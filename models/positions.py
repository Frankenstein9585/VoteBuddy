from models.base_model import BaseModel
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

from config import db


class Positions(BaseModel, db.Model):
    """User's Table"""
    __tablename__ = 'positions'
    title = db.Column(db.String(126), nullable=True)
    candidates = db.relationship('Candidate', back_populates='position')
    votes = db.relationship('Vote', back_populates='position')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
