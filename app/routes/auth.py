from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/register", methods=["POST"])
def register():
    return jsonify({"message": "Register route placeholder"})

@auth_bp.route("/api/login", methods=["POST"])
def login():
    return jsonify({"message": "Login route placeholder"})
