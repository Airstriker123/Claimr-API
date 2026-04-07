from flask import Blueprint, jsonify, request, Response
from app.services.register_user import RegisterUser
from app.services.login_user import LoginUser
from typing import Tuple

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register() -> Tuple[Response, int]:
    try:
        # request json data from client (username and password)
        username = request.json["username"]
        password = request.json["password"]
        return RegisterUser(username, password).register()
    except KeyError as e:
        print(f"[ERROR] failed to fetch username and password from client \n {e}")
    return jsonify({"status": "401"})


@auth_bp.route("/login", methods=["POST"])
def login() -> Tuple[Response, int]:
    try:
        # request json data from client (username and password)
        username = request.json["username"]
        password = request.json["password"]
        return LoginUser(username, password).login()
    except KeyError as e:
        print(f"[ERROR] failed to fetch username and password from client \n {e}")
    return jsonify({"status": "401"})
