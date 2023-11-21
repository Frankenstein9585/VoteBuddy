"""Register Form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from models import User


class RegisterForm(FlaskForm):
    """Handles registrations"""
    first_name = StringField('First Name*', validators=[DataRequired(), Length(min=3)])
    last_name = StringField('Last Name*', validators=[DataRequired(), Length(min=3)])
    matric_number = StringField('Matriculation Number*', validators=[DataRequired(), Length(max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_matric_number(self, matric_number):
        user = User.query.filter_by(matric_number=matric_number.data).first()
        if user:
            raise ValidationError('This matriculation number has already been registered')
