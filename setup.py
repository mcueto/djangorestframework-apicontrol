from distutils.core import setup

setup(
    name='rest_framework_apicontrol',
    packages=['rest_framework_apicontrol'],
    version='0.1.0',
    description='Django Rest Framework Library to control users over APIs',
    author='Marcelo Cueto',
    author_email='cueto@live.cl',
    url='https://github.com/mcueto/djangorestframework-apicontrol',
    download_url='https://github.com/mcueto/djangorestframework-auth0/tarball/0.1.0',
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
        'django>=1.10.0',
        'djangorestframework>=1.9.0'
    ],
)
