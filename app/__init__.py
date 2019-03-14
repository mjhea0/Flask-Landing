# app/__init__.py

import os

from flask import Flask, render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='static')
app.config.from_object(os.environ['APP_SETTINGS'])


login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)


from app.mod_main.views import main_blueprint  # noqa: E402
from app.mod_user.views import user_blueprint  # noqa: E402
from app.mod_api import api_blueprint  # noqa: E402

app.register_blueprint(main_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(api_blueprint)


from app.models import User  # noqa: E402

login_manager.login_view = "user.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500


@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403
