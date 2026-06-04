# Application entry file.
# constructs the application into a package (useful for docker bundling)


#——— <File imports (modules/external modules>———
from flask import Flask
from flask_cors import CORS
from flask_session import Session
from flask import jsonify
from flask_limiter.errors import RateLimitExceeded
import logging

# internal modules
from .utils.debug import warn
from .config import Config
from .extensions import db, bcrypt, limiter
from .routes import register_routes
#————— </File imports (end)/>—————————



#———<entry function to application  (initializes the app)>—————#
def main() -> Flask:
    """Main entry point for the application."""
    app: Flask = Flask("api.claimr.dev") # create  app flask object
    app.config.from_object(Config) #pull app config from Config class
    db.init_app(app) # Construct database (sql) using application
    bcrypt.init_app(app) # bcrypt construct
    Session(app) # session construct
    limiter.init_app(app) # ratelimit construct

    # Initializes Cross Origin Resource sharing for the application.
    CORS(
        app,
        supports_credentials=True,
        origins= \
        [
            # frontend vite server needs to run on port 9995 to allow connection between frontend and backend
            "http://localhost:9995",
            "http://192.168.68.112:4173"
        ]
    )

    register_routes(app) # register blueprint routes to application
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING) # prevent sql spam

    # Create tables that do not exist in the database by calling metadata.create_all() for all or some bind keys.
    # This does not update existing tables, use a migration library for that.
    with app.app_context():
        db.create_all()

    # Register a function to handle errors by code or exception class.
    # A decorator that is used to register a function given an error code.
    @app.errorhandler(RateLimitExceeded)
    def handle_ratelimit(e):
        warn("RATE LIMIT TRIGGERED")
        return jsonify({
            "error": "Too many requests. Please try again later."
        }), 429
    return app
#———<entry function to application  (initializes the app)/>—————#