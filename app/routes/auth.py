from flask import (
    Blueprint,
    jsonify,
    request,
    Response,
)
from app.services.auth.register_user_service import RegisterUserService
from app.services.auth.login_user_service import LoginUserService
from app.services.auth.get_current_user_service import GetCurrentUserService
from app.services.auth.wipe_session_service import WipeSessionService
from typing import Tuple, Any

auth_bp:Blueprint = Blueprint("auth", __name__, url_prefix="/api")

@auth_bp.route("/register", methods=["POST"])
def register() -> Tuple[Response, int] | int:
    try:
        # request json data from client (username and password)
        username: str = request.json["username"]
        password: str = request.json["password"]
        return RegisterUserService(
            username,
            password
        ).register()
    except Exception as e:
        print(f"[ERROR] failed to fetch username and password from client \n {e}")
    return 500


@auth_bp.route("/login", methods=["POST"])
def login() -> Tuple[Response, int] | int:
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
    return 500

@auth_bp.route("/@me", methods=["GET"])
def get_current_session() -> tuple[Any, int] | None | Any:
    try:
        return GetCurrentUserService().get_current_user()
    except Exception as e:
        print(f"[ERROR] failed to validate session \n {e}")
    return 500


@auth_bp.route("/logout", methods=["POST"])
def logout_current_session() -> tuple[dict[str, str], int] | int:
    try:
        return WipeSessionService().wipe_session()
    except Exception as e:
        print(f"[ERROR] failed to delete session \n {e}")
    return 500



