# app/mod_main/views.py

from flask import render_template, Blueprint, request, flash, redirect, url_for

from app.mod_main.forms import SignUpForm
from app import db
from app.models import Email

main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """Landing page for users to enter emails."""
    form = SignUpForm(request.form)
    if form.validate_on_submit():
        test = Email.query.filter_by(email=form.email.data).first()
        if test:
            flash('Sorry that email aleady exists!', 'danger')
        else:
            email = Email(email=form.email.data)
            db.session.add(email)
            db.session.commit()
            flash('Thank you for your interest!', 'success')
            return redirect(url_for('main.index'))
    return render_template('main/index.html', form=form)
