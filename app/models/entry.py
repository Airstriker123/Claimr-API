from ..extensions import db

class Entry(db.Model):
    """Table to record user entries id = pk relating what entry belongs to which user."""
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(100))
    date = db.Column(db.String(20))
    amount = db.Column(db.Float)
    tax = db.Column(db.Float)
    category = db.Column(db.String(50))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
