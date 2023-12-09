from models.base_model import BaseModel, db
from flask_bcrypt import Bcrypt
from flask_login import UserMixin



class Positions(BaseModel, db.Model):
    """User's Table"""
    __tablename__ = 'positions'
    title = db.Column(db.String(126), nullable=True)
    candidates = db.relationship('Candidate', secondary='candidate_position_association', back_populates='positions')
    votes = db.relationship('Vote', back_populates='position')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.title
