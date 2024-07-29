from models.base_model import BaseModel, db
from flask_bcrypt import Bcrypt
from flask_login import UserMixin



class Vote(BaseModel, db.Model):
    """User's Table"""
    __tablename__ = 'votes'
    user_id = db.Column(db.String(36, collation='utf8_bin'), db.ForeignKey('users.id'), nullable=False)
    candidate_id = db.Column(db.String(36, collation='utf8_bin'), db.ForeignKey('candidates.id'), nullable=False)

    user = db.relationship('User', back_populates='votes')
    candidate = db.relationship('Candidate', back_populates='votes')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
