from ..extensions import db

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, nullable=False)