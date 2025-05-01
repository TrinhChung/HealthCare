from database_init import db
from datetime import datetime

class HealthSurvey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    has_chronic_disease = db.Column(db.Boolean, default=False)
    smoking = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
