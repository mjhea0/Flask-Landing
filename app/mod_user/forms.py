# app/mod_user/forms.py


from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = TextField('Email Address', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
