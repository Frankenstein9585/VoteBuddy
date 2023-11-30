from models.base_model import BaseModel
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

from config import db


class User(BaseModel, db.Model, UserMixin):
    """User's Table"""
    __tablename__ = 'users'
    matric_number = db.Column(db.String(15), nullable=False, unique=True)
    first_name = db.Column(db.String(126), nullable=False)
    last_name = db.Column(db.String(126), nullable=False)
    password = db.Column(db.String(126), nullable=False)
    votes = db.relationship('Vote', back_populates='user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
