# from distutils.core import setup
from setuptools import setup

setup(
    name='rest_framework_apicontrol',
    packages=['rest_framework_apicontrol'],
    include_package_data=True,
    version='0.7.5',
    description='Django Rest Framework Library to control Client Apps over APIs',
    author='Marcelo Cueto',
    author_email='cueto@live.cl',
    url='https://github.com/mcueto/djangorestframework-apicontrol',
    download_url='https://github.com/mcueto/djangorestframework-auth0/tarball/0.7.5',
    keywords=['api', 'control', 'rest framework', 'django'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'django>=2.0.0',
        'djangorestframework>=3.7.0'
        'psycopg2>=2.7.3'
    ],
)
