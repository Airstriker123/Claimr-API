from flask import (
    jsonify,
    session,
    Response
)
from app.models.user import User
from typing import Union, Tuple, Any


class GetCurrentUserService(object):

    @staticmethod
    def get_current_user() -> Union[Response, Tuple[Response, int]]:
        # get the client user and check if they are authorized
        user_id: Any = session.get("user_id")
        if not user_id:
            # if user id is not found in session
            return jsonify(
                {
                    "error": "Unauthorized"
                }
            ), 401

        # if found do this
        user: Any = User.query.filter_by(id=user_id).first()  # query user from database

        if not user:
            return jsonify(
                {
                    "error": "User not found"
                }
            ), 401

        return jsonify(
        {
            "user": {
                "id": user.id,
                "username": user.username
            }
        }), 200

