from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g
from app import app, db
from forms import SignupForm
from app.module.models import Email

mod = Blueprint('landing', __name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """landing page for users to enter emails"""
    form = SignupForm(request.form)
    if form.validate_on_submit():
        email = Email()
        form.populate_obj(email)
        db.session.add(email)
        db.session.commit()
        flash(u'Thank you for your interest!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


@app.route('/view', methods=['GET'])
def view_signups():
    """displays submitted emails to the admin"""
    if not session.get('logged_in'):
        return "Scram, kiddo."
    signups = Email.query.all()
    return render_template('view_signups.html', signups=signups)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page for admins to login"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('view_signups'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    """logout for admins"""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))