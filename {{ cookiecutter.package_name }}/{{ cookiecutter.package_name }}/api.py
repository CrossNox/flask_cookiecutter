"""API module."""
from flask_restx import Api
from {{cookiecutter.package_name}} import __version__
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


api = Api(prefix="/v1", version=__version__)
