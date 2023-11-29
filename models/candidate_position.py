from models.base_model import BaseModel
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

from config import db


class CandidatePosition(BaseModel, db.Model):
    """Candidate's Model"""
    __tablename__ = 'candidate_position'
    position_id = db.Column(db.String(36, collation='utf8_bin'), db.ForeignKey('positions.id'), nullable=False)
    candidate_id = db.Column(db.String(36, collation='utf8_bin'), db.ForeignKey('candidates.id'), nullable=False)
    vote_count = db.Column(db.Integer, nullable=False, default=0)

    candidate = db.relationship('Candidate', back_populates='positions')
    position = db.relationship('Positions', back_populates='candidates')

    # candidate_position_relationship = db.Table('candidate_position_relationship',
    #                                            db.Column('candidate_id', db.String(36, collation='utf8_bin'), db.ForeignKey('candidates.id')),
    #                                            db.Column('position_id', db.String(36, collation='utf8_bin'), db.ForeignKey('positions.id'))
    #                                            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)