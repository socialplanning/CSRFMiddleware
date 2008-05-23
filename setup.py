try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='csrfmiddleware',
    version="",
    #description='',
    #author='',
    #author_email='',
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
