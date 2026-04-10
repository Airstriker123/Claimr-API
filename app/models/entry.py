from ..extensions import db

class Entry(db.Model):
    """Table to record user entries id = pk relating what entry belongs to which user."""
    __tablename__: str = 'entries'
    id: int = db.Column(db.Integer, primary_key=True)
    merchant: str = db.Column(db.String(100))
    date: str = db.Column(db.String(20))
    amount: float = db.Column(db.Float)
    tax: float = db.Column(db.Float)
    category: str = db.Column(db.String(50))
    description: str = db.Column(db.Text)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'))
