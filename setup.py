try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='csrfmiddleware',
    version="1.3",
    description="CSRF Middleware for Pylons, based on Luke Plant's django version.",
    author='Luke Plant and David Turner',
    author_email='novalis@openplans.org',
    #url='',
    install_requires=["Paste",
                      "beaker",
                      "webob",
                      ],
    entry_points="""
    # -*- Entry points: -*-
    [paste.filter_factory]
    csrf = csrfmiddleware:make_csrf_filter
    [paste.filter_app_factory]
    csrf = csrfmiddleware:make_csrf_filter_app
    """,
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'csrfmiddleware': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'csrfmiddleware': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},

)
