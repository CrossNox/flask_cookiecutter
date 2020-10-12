"""Flask api."""
from flask import Flask
from flask_migrate import Migrate

from {{cookiecutter.package_name}}.api import api
from {{cookiecutter.package_name}}.cfg import config
from {{cookiecutter.package_name}}.models import db


def create_app():
    """creates a new app instance"""
    new_app = Flask(__name__)
    new_app.config["SQLALCHEMY_DATABASE_URI"] = config.database.url(
        default="sqlite:///{{cookiecutter.package_name}}.db"
    )
    new_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(new_app)
    api.init_app(new_app)
    Migrate(new_app, db)
    return new_app
