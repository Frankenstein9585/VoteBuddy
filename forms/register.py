"""Register Form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from models import User


class RegisterForm(FlaskForm):
    """Handles registrations"""
    matric_number = StringField('Matriculation Number', validators=[DataRequired(), Length(max=11)])
    first_name = StringField('Matriculation Number', validators=[DataRequired(), Length(max=50)])
    middle_name = StringField('Matriculation Number', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Matriculation Number', validators=[DataRequired(), Length(max=50)])
    level = StringField('Matriculation Number', validators=[DataRequired(), Length(max=3)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_matric_number(self, matric_number):
        user = User.query.filter_by(matric_number=matric_number.data).first()
        if user and user.has_registered:
            raise ValidationError('This matriculation number has already been registered')
