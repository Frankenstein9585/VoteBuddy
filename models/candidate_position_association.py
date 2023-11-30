from config import db
from models.base_model import BaseModel


class CandidatePositionAssociation(BaseModel, db.Model):
    """Candidate_Position_Association Model"""
    __tablename__ = 'candidate_position_association'
    candidate_id = db.Column(db.String(36, collation='utf8_bin'), db.ForeignKey('candidates.id'), nullable=False)
    position_id = db.Column(db.String(36, collation='utf8_bin'), db.ForeignKey('positions.id'), nullable=False)
    vote_count = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
