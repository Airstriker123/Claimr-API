import os
from dotenv import load_dotenv

load_dotenv() #load environment file

class Config:
    """ORM Database configuration"""
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_ECHO: bool = False  # prevent SQL message nuking in terminal (let this be True if you want to see sql code injection in the database through terminal
    SESSION_TYPE: str = "filesystem"  # store as local
    SESSION_PERMANENT: bool = False
    SESSION_USE_SIGNER: bool = True  # session storage
    SESSION_COOKIE_SECURE: bool = False
    SESSION_COOKIE_SAMESITE: str = 'Lax'
    SESSION_COOKIE_HTTPONLY: bool = True