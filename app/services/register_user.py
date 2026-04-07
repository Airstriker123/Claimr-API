from ..models.user import User
from ..extensions import db, bcrypt
from flask import jsonify, session, Response
from typing import Union, Tuple


class RegisterUser(object):

    def __init__(self,
                 username:str,
                 password:str
                 ):
        self.__username = username
        self.__password_hash = password

    def register(self) -> Tuple[Response, int]:
        try:
            if self.__username_unique():
                hashed_password = self.__hash_password()
                if hashed_password == "": return jsonify({"err": "hash failed"}), 401
                print("[SUCCESS] user registered")
                # store user id in session
                new_user = User(
                    username=self.__username,
                    password=hashed_password
                )
                db.session.add(new_user)
                db.session.commit()
                session["user_id"] = new_user.id

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
            print(f"[ERROR] failed to register user\n{e}")
        return jsonify({"status": "401"})


    def __username_unique(self) -> bool:
        try:
            # CHECK IF USER EXISTS IN DATABASE
            __user_exits = User.query.filter_by(username=self.__username).first() is not None
            if __user_exits:
                print("[!] register failed - user already exists")
                return False # if they do exist, notify client that user exists and prevent duplicate accounts
            return True # if unique username_unique = true
        except Exception as e:
            print(f"[ERROR] failed to perform SQL query in database \n {e}")
        return False

    def __hash_password(self) -> str:
        try:
            # ---- security methods (encryption/hasing passwords) ----#
            self.__hashed_password = bcrypt.generate_password_hash(self.__password_hash).decode("utf-8")
            return self.__hashed_password
            # ---- </security methods> ----#
        except Exception as e:
            print(f"[ERROR] failed to perform hashing/encrypting of account \n {e}")
        return jsonify({"status": "401"})



