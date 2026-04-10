from flask import (
    Blueprint,
    jsonify,
    request,
    Response,
)
from app.services.register_user_service import RegisterUserService
from app.services.login_user_service import LoginUserService
from typing import Tuple

auth_bp:Blueprint = Blueprint("auth", __name__, url_prefix="/api")

@auth_bp.route("/register", methods=["POST"])
def register() -> Tuple[Response, int]:
    try:
        # request json data from client (username and password)
        username: str = request.json["username"]
        password: str = request.json["password"]
        return RegisterUserService(
            username,
            password
        ).register()

    except KeyError as e:
        print(f"[ERROR] failed to fetch username and password from client \n {e}")
    return jsonify(
        {
            "error": "route error",
            "status": 400
        }
    )


@auth_bp.route("/login", methods=["POST"])
def login() -> Tuple[Response, int]:
    try:
        # request json data from client (username and password)
        username: str = request.json["username"]
        password: str = request.json["password"]
        return LoginUserService(
            username,
            password
        ).login()

    except KeyError as e:
        print(f"[ERROR] failed to fetch username and password from client \n {e}")
    return jsonify(
        {
            "error": "route error",
            "status": 400
        }
    )
