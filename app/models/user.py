from ..extensions import db
from uuid import uuid4

def get_uuid() -> str:
    return uuid4().hex #unique user id for each user

class User(db.Model):
    """Table to store user information about uuid, username and hashed password."""
    __tablename__: str = "users"  # name
    # table fields, colums (converts to sql)
    id: str = db.Column(db.String(32),  # uuid string length
                   primary_key=True,
                   unique=True,
                   default=get_uuid
                   )  # uuid of each account

    username: str = db.Column(db.String(345),
                         unique=True)  # username field
    password_hash: str = db.Column(db.Text,
                         nullable=False)  # password field
