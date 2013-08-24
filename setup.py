"""
Flask-Landing
----------------

Basic Landing Page for collecting emails. Built with Flask.

Links
`````

* `repo <https://github.com/mjhea0/Flask-Landing>`_

"""
import app
from setuptools import setup

setup(
    name='Flask-Landing',
    version=app.__version__,
    url='https://github.com/mjhea0/Flask-Landing',
    license='Apache Software License',
    author='Michael Herman',
    author_email='michael@mherman.org',
    tests_require=['pytest'],
    install_requires=['Flask==0.10.1',
                    'Flask-WTF==0.8.4',
                    'WTForms==1.0.4',
                    'Flask-SQLAlchemy==1.0',
                    'coverage==3.6',
                    'nose==1.3.0',
                    'selenium==2.35.0',
                    ],
    description='Landing page for collecting emails.',
    #long_description=long_description,
    packages=['app'],
    include_package_data=True,
    platforms='any',
    test_suite='app.tests.landing_tests.py',
    classifiers = [
        'Programming Language :: Python',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)