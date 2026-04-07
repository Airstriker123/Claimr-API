from flask import Blueprint, jsonify, request, Response
from app.services.register_user import RegisterUser
from typing import Tuple

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/register", methods=["POST"])
def register() -> Tuple[Response, int] | bool:
    try:
        # request json data from client (username and password)
        username = request.json["username"]
        password = request.json["password"]
        return RegisterUser(username, password).register()
    except KeyError as e:
        print(f"[ERROR] failed to fetch username and password from client \n {e}")
        return False

@auth_bp.route("/api/login", methods=["POST"])
def login():
    return jsonify({"message": "Login route placeholder"})
