from models.base_model import BaseModel
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

from app import db


class Candidate(BaseModel, db.Model):
    """Candidate's Model"""
    __tablename__ = 'candidates'
    matric_number = db.Column(db.String(15), nullable=False, unique=True)
    first_name = db.Column(db.String(126), nullable=False)
    last_name = db.Column(db.String(126), nullable=False)
    image = db.Column(db.String(126), nullable=True)
    faculty = db.Column(db.String(126), nullable=True)
    department = db.Column(db.String(126), nullable=True)
    programme = db.Column(db.String(126), nullable=True)
    votes = db.relationship('Vote', back_populates='candidate')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

