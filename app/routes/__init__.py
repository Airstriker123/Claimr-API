from .auth import auth_bp
from .entries import entries_bp
from .home import home_bp

def register_routes(app) -> None:
    app.register_blueprint(auth_bp)
    app.register_blueprint(entries_bp)
    app.register_blueprint(home_bp)


