from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


# view limiter config options -- https://flask-limiter.readthedocs.io/en/stable/#configuring-a-storage-backend
limiter: Limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per minute", "1 per second"]
    #storage_uri="redis://localhost:6379", -- in production a redis instancee must exist (removed to avoid using docker in dev)
)
db: SQLAlchemy = SQLAlchemy()
bcrypt: Bcrypt = Bcrypt()
