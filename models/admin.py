from models.base_model import BaseModel
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

from config import db, login_manager


class Admin(BaseModel, db.Model, UserMixin):
    """User's Table"""
    __tablename__ = 'admins'
    first_name = db.Column(db.String(126), nullable=False)
    last_name = db.Column(db.String(126), nullable=False)
    username = db.Column(db.String(126), nullable=False)
    password = db.Column(db.String(126), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
