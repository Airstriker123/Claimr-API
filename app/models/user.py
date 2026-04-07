from ..extensions import db

class User(db.Model):
    __tablename__ = "users"  # name
    # table fields, colums (converts to sql)
    id = db.Column(db.String(32),  # uuid string length
                   primary_key=True,
                   unique=True,
                   default=get_uuid
                   )  # uuid of each account

    username = db.Column(db.String(345),
                         unique=True)  # username field
    password_hash = db.Column(db.Text,
                         nullable=False)  # password field
