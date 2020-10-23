"""Flask api."""
from pathlib import Path

from flask import Flask
from flask_migrate import Migrate

from {{cookiecutter.package_name}}.api import api
from {{cookiecutter.package_name}}.cfg import config
from {{cookiecutter.package_name}}.models import db

from werkzeug.middleware.proxy_fix import ProxyFix

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def fix_dialect(s):
    if s.startswith("postgres://"):
        s = s.replace("postgres://", "postgresql://")
    s = s.replace("postgresql://", "postgresql+psycopg2://")
    return s


def create_app():
    """creates a new app instance"""
    new_app = Flask(__name__)
    new_app.config["SQLALCHEMY_DATABASE_URI"] = config.database.url(
        default="sqlite:///{{cookiecutter.package_name}}.db", cast=fix_dialect
    )
    new_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(new_app)
    api.init_app(new_app)
    Migrate(new_app, db, directory=Path(__file__).parent / "migrations")
    new_app.wsgi_app = ProxyFix(
        new_app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1
    )  # remove after flask-restx > 0.2.0 is released
    # https://github.com/python-restx/flask-restx/issues/230
    return new_app
