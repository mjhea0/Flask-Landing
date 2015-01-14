# project/main/forms.py


from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Email, length


class SignUpForm(Form):
    email = TextField(
        'Enter your email address',
        validators=[DataRequired(), Email(), length(min=3)])
