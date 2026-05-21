from app.models.user import User
from app.extensions import db, bcrypt
from app.utils.debug import success, error_crash, client_error

import re
from flask import (
    jsonify,
    session,
    Response,
)
from typing import Tuple


class RegisterUserService(object):
    """Backend logic class for registering users to database"""


    def __init__(self, username:str,password:str) -> None:
        """Constructor for RegisterUserService"""
        self.__username: str = username.strip()
        self.__password: str = password.strip()


    def register(self) -> tuple[Response, int] | Response:
        """Method for registering user"""
        try:
            if self.__username_unique(): # check if username exists in records
                hashed_password: str | bool = self.__hash_password()
                if not hashed_password: # check if password was hashed
                    client_error("password not meet requirements!")
                    return jsonify(
                        {
                            "error": "Password does not meet requirements!"
                        }
                    ), 401
                success(f"Successfully registered user {self.__username}") # print this if success
                # store user id in session
                new_user: User = User(
                    username=self.__username,
                    password_hash=hashed_password
                )
                # commit user to database
                db.session.add(new_user)
                db.session.commit()
                session["user_id"]: str = new_user.id

                # return JSON data to client for storage
                return jsonify(
                    {
                        "id": new_user.id,
                        "username": self.__username,
                    }
                ), 200
            return jsonify({
                "error": "username taken",

            }), 400
        except Exception as e:
            error_crash(e)
        return jsonify({"status": "500"})


    def __username_unique(self) -> bool:
        """Method for checking if username already exists"""
        try:
            # CHECK IF USER EXISTS IN DATABASE
            __user_exists: bool = User.query.filter_by(username=self.__username).first() is not None
            if __user_exists:
                print("[!] register failed - user already exists")
                return False # if they do exist, notify client that user exists and prevent duplicate accounts
            return True # if unique username_unique = true
        except Exception as e:
            print(f"[ERROR] failed to perform SQL query in database \n {e}")
        return False



    def __check_valid_password(self) -> bool:
        """Method for checking if password is valid and meets requirements"""
        # pattern to query using regex
        pattern = (
            r"^(?=.*[A-Z])"
            r"(?=.*[a-z])"
            r"(?=.*\d)"
            r"(?=.*[@#$%^&+=!]).{10,20}$"
        )
        is_valid = bool(re.match(
            pattern,
            self.__password)
        ) # query with pattern using regex
        if self.__password == "": # if no input
            is_valid = False
        return is_valid


    def __hash_password(self) -> str | bool:
        """Method for hashing password the password"""
        try:
            # ---- security methods (encryption/hashing passwords, password checker) ----#
            if not self.__check_valid_password(): # check if password meets security requirements
                return False
            # hash password
            self.__hashed_password: str = bcrypt.generate_password_hash(self.__password).decode("utf-8") # bcrypt auto salts passwords
            return self.__hashed_password
            # ---- </security methods> ----#
        except Exception as e:
            print(f"[ERROR] failed to perform hashing/encrypting of account \n {e}")
        return False

