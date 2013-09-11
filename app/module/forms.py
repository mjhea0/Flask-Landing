from flask.ext.wtf import Form, TextField, validators, fields


class SignupForm(Form):
	email = fields.TextField('Enter your email address', validators=[validators.required()])
