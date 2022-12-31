import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager  # ? Import LoginManager

login_manager = LoginManager()  # ? Create an instance of LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = "verysecretkey"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)  # ? Initialize LoginManager
LoginManager.login_view = "login"  # ? Set the login view
