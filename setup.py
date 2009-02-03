try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='csrfmiddleware',
    version="1.0",
    description="CSRF Middleware for Pylons, based on Luke Plant's django version.",
    author='Luke Plant and David Turner',
    author_email='novalis@openplans.org',
    #url='',
    install_requires=["Paste",
                      "WSGIFilter"
                      ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'csrfmiddleware': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'csrfmiddleware': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},

)
