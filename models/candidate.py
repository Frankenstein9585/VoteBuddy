from models.base_model import BaseModel, db
from flask_bcrypt import Bcrypt
from flask_login import UserMixin


class Candidate(BaseModel, db.Model):
    """Candidate's Model"""
    __tablename__ = 'candidates'
    # matric_number = db.Column(db.String(15), nullable=False, unique=True)
    # first_name = db.Column(db.String(126), nullable=False)
    # last_name = db.Column(db.String(126), nullable=False)
    name = db.Column(db.String(126), nullable=False)
    # image = db.Column(db.String(126), nullable=True)
    faculty = db.Column(db.String(126), nullable=True)
    department = db.Column(db.String(126), nullable=True)
    programme = db.Column(db.String(126), nullable=True)
    # vote_count = db.Column(db.Integer, nullable=False, default=0)
    positions = db.relationship('Positions', secondary='candidate_position_association', back_populates='candidates')
    votes = db.relationship('Vote', back_populates='candidate')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name
