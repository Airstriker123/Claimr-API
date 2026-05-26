from ..extensions import db
from typing import Any

class Entry(db.Model):
    """
    Database model for a tax deduction entry.
    Stores merchant details, amounts, tax, and warranty information.
    """
    __tablename__: str = 'entries'

    # Primary key and core details
    id: Any = db.Column(db.Integer, primary_key=True)
    merchant: Any = db.Column(db.String(100))
    date: Any = db.Column(db.DateTime)
    amount: Any = db.Column(db.Float)
    tax: Any = db.Column(db.Float)
    
    # Classification and description
    category: Any = db.Column(db.String(50))
    description: Any = db.Column(db.Text)
    
    # Optional warranty tracking
    warranty_months: Any = db.Column(db.Integer, nullable=True)
    warranty_expiry_date: Any = db.Column(db.DateTime, nullable=True)
    
    # Metadata and relationship
    created_at: Any = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id: Any = db.Column(db.Integer, db.ForeignKey('users.id'))



