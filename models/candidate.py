from models.base_model import BaseModel
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

from config import db


class Candidate(BaseModel, db.Model):
    """Candidate's Model"""
    __tablename__ = 'candidates'
    position_id = db.Column(db.String(36, collation='utf8_bin'), db.ForeignKey('positions.id'), nullable=False)
    matric_number = db.Column(db.String(15), nullable=False, unique=True)
    first_name = db.Column(db.String(126), nullable=False)
    last_name = db.Column(db.String(126), nullable=False)
    image = db.Column(db.String(126), nullable=True)
    faculty = db.Column(db.String(126), nullable=True)
    department = db.Column(db.String(126), nullable=True)
    programme = db.Column(db.String(126), nullable=True)
    position = db.relationship('Positions', back_populates='candidates')
    votes = db.relationship('Vote', back_populates='candidate')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
