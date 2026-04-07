import os
from dotenv import load_dotenv

load_dotenv() #load environment file

class Config:
    """ORM Database configuration"""
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # prevent SQL message nuking in terminal (let this be True if you want to see sql code injection in the database through terminal
    SESSION_TYPE = "filesystem"  # store as local
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True  # session storage
