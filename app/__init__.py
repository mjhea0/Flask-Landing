from flask import Flask, render_template, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) 
app.config.from_object('config')

db = SQLAlchemy(app) 

from app.module.views import mod as landingModule
app.register_blueprint(landingModule)

__version__ = '0.1.0'

#----------------------------------------
# controllers
#----------------------------------------

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
