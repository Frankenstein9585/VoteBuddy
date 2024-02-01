"""Register Form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    """Handles registrations"""
    matric_number = StringField('Matriculation Number', validators=[DataRequired(), Length(max=11)])
    submit = SubmitField('Login')
