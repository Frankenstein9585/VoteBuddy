from models.base_model import BaseModel
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

from app import db


class Vote(BaseModel, db.Model):
    """User's Table"""
    __tablename__ = 'votes'
    user_id = db.Column(db.String(126), db.ForeignKey('users.id'), nullable=False)
    candidate_id = db.Column(db.String(126), db.ForeignKey('candidates.id'), nullable=False)
    position_id = db.Column(db.String(126), db.ForeignKey('positions.id'), nullable=False)
    user = db.relationship('User', back_populates='votes')
    candidate = db.relationship('Candidate', back_populates='votes')
    position = db.relationship('Position', back_populates='votes')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

