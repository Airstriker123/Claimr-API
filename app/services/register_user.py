from ..models.user import User
from ..extensions import db, bcrypt
from flask import jsonify, session, Response

class RegisterUser(object):
    """
BEGIN RegisterUser(username,password)
        username = get input from user
        password = get input from user
        UniqueUser() = check if username is unique
        IF UniqueUser() THEN
            append username,password to Users()
            DISPLAY "account created"
            session = generate a uuid and append to localstorage()
            renderapp = redirect to homepage() with login(username,password)
        ELSE
            DISPLAY "username taken!"
        ENDIF
END RegisterUser(username,password)
    """
    def __init__(self,
                 username:str,
                 password:str
                 ):
        self.__username = username
        self.__password = password

    def register(self) -> tuple[Response, int] | bool:
        try:
            if self.__username_unique():
                hashed_password = self.__hash_password()
                if hashed_password == "": return False
                print("[SUCCESS] user registered")
                # store user id in session
                new_user = User(username=self.__username, password=hashed_password)
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
            return jsonify(
            {
                "message": "register failed",
            }
        ), 500


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

    def __hash_password(self) -> str | bool:
        try:
            # ---- security methods (encryption/hasing passwords) ----#
            self.__hashed_password = bcrypt.generate_password_hash(self.__password).decode("utf-8")
            return self.__hashed_password
            # ---- </security methods> ----#
        except Exception as e:
            print(f"[ERROR] failed to perform hashing/encrypting of account \n {e}")
            return False


