from flask import (
    Blueprint,
    request,
    Response,
    jsonify
)
from app.services.auth.register_user_service import RegisterUserService
from app.services.auth.login_user_service import LoginUserService
from app.services.auth.get_current_user_service import GetCurrentUserService
from app.services.auth.wipe_session_service import WipeSessionService
from app.extensions import limiter
from typing import Tuple, Any

auth_bp:Blueprint = Blueprint("auth", __name__, url_prefix="/api")

@auth_bp.route("/register", methods=["POST"])
@limiter.limit("1/second;") #prevent account spams on ip
def register() -> Tuple[Response, int]:
    """Route to register a new user to database"""
    try:
        # request json data from client (username and password)
        username: str = request.json["username"]
        password: str = request.json["password"]
        return RegisterUserService(
            username,
            password
        ).register() #get from service
    except Exception as e:
        print(f"[ERROR] failed to fetch username and password from client \n {e}")
        return jsonify(
            {
                "error": "Internal Server Error"
            }
        ), 500


@auth_bp.route("/login", methods=["POST"])
@limiter.limit("5/minute;1/second")
def login() -> Tuple[Response, int]:
    """Route to Login a new user to application"""
    try:
        # request json data from client (username and password)
        username: str = request.json["username"]
        password: str = request.json["password"]
        return LoginUserService(
            username,
            password
        ).login()
    except Exception as e:
        print(f"[ERROR] failed to fetch username and password from client \n {e}")
        return jsonify(
            {
                "error": "Internal Server Error"
            }
        ), 500

@auth_bp.route("/@me", methods=["GET"])
@limiter.limit("100/minute;3/second")
def get_current_session() -> tuple[Any, int]:
    """Route to get current session for current user
    and return a session id to client"""
    try:
        return GetCurrentUserService().get_current_user()
    except Exception as e:
        print(f"[ERROR] failed to validate session \n {e}")
        return jsonify(
            {
                "error": "Internal Server Error"
            }
        ), 500


@auth_bp.route("/logout", methods=["POST"])
def logout_current_session() -> tuple[Any, int]:
    """Route to logout current session from client"""
    try:
        return WipeSessionService().wipe_session()
    except Exception as e:
        print(f"[ERROR] failed to delete session \n {e}")
        return jsonify(
            {
                "error": "Internal Server Error"
            }
        ), 500



