from flask.ext.wtf import Form, TextField, validators, fields


class SignupForm(Form):
	email = fields.TextField('Email address', validators=[validators.required()])
