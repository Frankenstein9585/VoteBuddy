"""Admin Creation Form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

from models import Admin


class AdminRegisterForm(FlaskForm):
    """Handles Admin Registration"""
    first_name = StringField('First Name*', validators=[DataRequired(), Length(min=3)])
    last_name = StringField('Last Name*', validators=[DataRequired(), Length(min=3)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Admin')


class AdminLoginForm(FlaskForm):
    """Handles Admin Login"""
    username = StringField('Username', validators=[DataRequired(), Length(max=11)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')
