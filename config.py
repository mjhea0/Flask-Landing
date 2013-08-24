import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'SecretKeyForSessionSigning'

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

USERNAME = "admin"
PASSWORD = "admin"

DATABASE = 'sample.db'
DATABASE_PATH = os.path.join(_basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
