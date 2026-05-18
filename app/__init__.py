from flask import Flask
from flask_cors import CORS
from flask_session import Session
from flask import jsonify
from flask_limiter.errors import RateLimitExceeded
import logging
from .utils.debug import warn

from .config import Config
from .extensions import db, bcrypt, limiter
from .routes import register_routes



def main() -> Flask:
    app: Flask = Flask("api.claimr.dev")
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    Session(app)
    limiter.init_app(app)

    CORS(
        app,
        supports_credentials=True,
        origins= \
        [
            "https://claimr.dev",
            "http://localhost:9995",
            "http://192.168.68.112:4173"
        ]
    )

    register_routes(app)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

    with app.app_context():
        db.create_all()

    @app.errorhandler(RateLimitExceeded)
    def handle_ratelimit(e):
        warn("RATE LIMIT TRIGGERED")
        return jsonify({
            "error": "Too many requests. Please try again later."
        }), 429


    return app