# app/models.py


import datetime
from sqlalchemy import UniqueConstraint

from app import db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return 'user email is {0}'.format(self.email)


class Email(db.Model):

    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, nullable=False)
    email_added_on = db.Column(db.DateTime, nullable=False)
    source = db.Column(db.String)
    form_data_as_json = db.Column(db.String)

    __table_args__ = (UniqueConstraint('email', 'source', name='_email_source_unique_contraint'),)

    def __init__(self, email, source=None, form_data_as_json=None):
        self.email = email
        self.form_data_as_json = form_data_as_json if form_data_as_json else None
        self.source = source if source else None
        self.email_added_on = datetime.datetime.now()
