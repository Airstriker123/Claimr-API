from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


# view limiter config options -- https://flask-limiter.readthedocs.io/en/stable/#configuring-a-storage-backend
limiter: Limiter = Limiter(
    key_func=get_remote_address,
)
db: SQLAlchemy = SQLAlchemy() # Integrates SQLAlchemy with Flask.
bcrypt: Bcrypt = Bcrypt() #Bcrypt class container for password hashing and checking logic using bcrypt.
