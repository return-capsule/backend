import logging
import boto3, botocore
import mongoengine

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from app.config import Config
from app.views import Router


def create_app():
    app_ = Flask(__name__)
    app_.config.from_object(Config)

    Router().init_app(app_)

    logging.getLogger('flask_cors').level = logging.DEBUG
    CORS(app_, resources={
        r"/*": {"origins": "*"}
    })
    JWTManager().init_app(app_)

    mongoengine.connect(
        'memories',
        username=app_.config['MONGODB_USERNAME'],
        password=app_.config['MONGODB_PASSWORD'],
        authentication_source='admin'
    )

    return app_


app = create_app()
