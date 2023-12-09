"""Register Form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from models import User


class RegisterForm(FlaskForm):
    """Handles registrations"""
    matric_number = StringField('Matriculation Number*', validators=[DataRequired(), Length(max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    image_byte_string = HiddenField('Image Byte String', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_matric_number(self, matric_number):
        user = User.query.filter_by(matric_number=matric_number.data).first()
        if user.has_registered:
            raise ValidationError('This matriculation number has already been registered')
