"""
Cross Site Request Forgery Middleware.

This is a middleware that implements protection against request
forgeries from other sites.

This is a Pylons port of Luke Plant's django version.

"""
from paste.wsgiwrappers import WSGIRequest
from wsgifilter import Filter
import re
import itertools

_ERROR_MSG = '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><body><h1>403 Forbidden</h1><p>Cross Site Request Forgery detected. Request aborted.</p></body></html>'

_POST_FORM_RE = \
    re.compile(r'(<form\W[^>]*\bmethod=(\'|"|)POST(\'|"|)\b[^>]*>)', re.IGNORECASE)
    
_HTML_TYPES = ('text/html', 'application/xhtml+xml')    

class CsrfMiddleware(Filter):
    """Pylons middleware that adds protection against Cross Site
    Request Forgeries by adding hidden form fields to POST forms and 
    checking requests for the correct value.  
      
    """

    def __init__(self, app, config):
        Filter.__init__(self, app)
        self.unprotected_path = config.get('csrf.unprotected_path')

    def __call__(self, environ, start_response):
        request = WSGIRequest(environ)
        session = environ['beaker.session']
        session.save() 

        if request.method == 'POST':
            if self.unprotected_path is not None:
                if request.path_info.startswith(self.unprotected_path):
                    return Filter.__call__(self, environ, start_response)
            try:
                session_id = session.id
            except KeyError:
                # No session, no check required
                return None

            csrf_token = session_id
            # check incoming token
            try:
                request_csrf_token = request.POST['csrfmiddlewaretoken']
            except KeyError:
                start_response("403 Forbidden", [])
                return [_ERROR_MSG]
            
            if request_csrf_token != csrf_token:
                start_response("403 Forbidden", [])
                return [_ERROR_MSG]
                
        return Filter.__call__(self, environ, start_response)

    def filter(self, environ, headers, data):
        session = environ['beaker.session']
        headers = dict(headers)
        csrf_token = session.id
        if csrf_token is not None and \
                headers['content-type'].split(';')[0] in _HTML_TYPES:
            
            # ensure we don't add the 'id' attribute twice (HTML validity)
            idattributes = itertools.chain(("id='csrfmiddlewaretoken'",), 
                                            itertools.repeat(''))
            def add_csrf_field(match):
                """Returns the matched <form> tag plus the added <input> element"""
                return match.group() + "<div style='display:none;'>" + \
                "<input type='hidden' " + idattributes.next() + \
                " name='csrfmiddlewaretoken' value='" + csrf_token + \
                "' /></div>"

            # Modify any POST forms
            data = _POST_FORM_RE.sub(add_csrf_field, data)
        return data
