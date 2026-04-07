from flask import Flask
from flask_cors import CORS
from flask_session import Session
import logging

from .config import Config
from .extensions import db, bcrypt
from .routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    Session(app)

    CORS(
        app,
        supports_credentials=True,
        origins=["https://claimr.dev"]
    )

    register_routes(app)

    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

    with app.app_context():
        db.create_all()

    return app