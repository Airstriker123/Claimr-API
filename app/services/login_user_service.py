from ..models.user import User
from flask import (
    jsonify,
    session,
    Response
)
from ..extensions import bcrypt

class LoginUserService(object):

    def __init__(self, username:str, password:str) -> None:
        self.username: str = username
        self.password: str = password
        self.user: User = User.query.filter_by(username=self.username).first()

    def login(self) -> tuple[Response, int]:
        try:
            user: User = self.user
            if not self.valid_username() or not self.valid_password():
                return jsonify({"message": "Invalid username or password"}), 401
            print("[SUCCESS] A USER LOGGED IN!")
            session["user_id"]: int = user.id  # store user id in session
            # return to client user id and username
            return jsonify(
                {
                    "id": user.id,
                    "username": user.username,
                }
            ), 200
        except Exception as e:
            print(f"[ERROR] {e}")
        return jsonify({"message": "server down"}), 401

    def valid_password(self) -> bool:
        # check if password is correct
        if self.user is None:
            return False #prevent crash if user is none
        if not bcrypt.check_password_hash(self.user.password_hash, self.password):
            return False
        return True

    def valid_username(self) -> bool:
        if self.user is None:  # if requested username and password not found
            return False
        return True

