from ..extensions import db
from typing import Any

class Entry(db.Model):
    """Table to record user entries id = pk relating what entry belongs to which user."""
    __tablename__: str = 'entries' #name
    #fields of table
    id: Any = db.Column(db.Integer, primary_key=True)
    merchant: Any = db.Column(db.String(100))
    date: Any = db.Column(db.DateTime)
    amount: Any = db.Column(db.Float)
    tax: Any = db.Column(db.Float)
    category: Any = db.Column(db.String(50))
    description: Any = db.Column(db.Text)
    user_id: Any = db.Column(db.Integer, db.ForeignKey('users.id'))



