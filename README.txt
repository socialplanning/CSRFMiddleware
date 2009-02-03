CSRFMiddleware
==============

Cross Site Request Forgery middleware allows you to create forms without having
to worry about cross site attacks. Simply add the CSRFMiddleware to your wsgi
pipeline, and the CSRFMiddleware will take care of the rest. It adds a token to
all forms, and verifies that the token matches upon submission.
