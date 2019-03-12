# app/mod_user/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, \
    redirect, flash, request, Response
from flask_login import login_user, logout_user, \
    login_required

from app import bcrypt
from app.models import User, Email
from app.mod_user.forms import LoginForm


################
#### config ####
################

user_blueprint = Blueprint('user', __name__,)


################
#### routes ####
################

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """Login page for admins."""
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('You are logged in. Welcome!', 'success')
            return redirect(url_for('user.admin'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form=form)
    return render_template('user/login.html', form=form)


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out. Bye!', 'success')
    return redirect(url_for('main.index'))


@user_blueprint.route('/admin')
@login_required
def admin():
    """Displays submitted emails to the admin."""
    signups = Email.query.all()
    return render_template('user/admin.html', signups=signups)

@user_blueprint.route('/embed-code')
@login_required
def embed_code():
    """Displays ajax based form."""
    return render_template('user/embed-code.html')

@user_blueprint.route('/download-emails')
@login_required
def download_emails():
    """Downloads emails."""
    signups = Email.query.all()
    def generate_csv():
        for e in signups:
            yield ','.join([e.email,str(e.email_added_on)])+'\n'
    response = Response(generate_csv(), mimetype='text/csv')
    response.headers.set(
        'Content-Disposition', 'attachment', filename='emails.csv')
    return response