"""Register Form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    """Handles registrations"""
    matric_number = StringField('Matriculation Number', validators=[DataRequired(), Length(max=11)])
    degrees = [
        ('', 'Please select an option'),
        ('B.A. English', 'B.A. English'),
        ('B.A. Philosophy', 'B.A. Philosophy'),
        ('B.Eng. Computer Engineering', 'B.Eng. Computer Engineering'),
        ('B.NSc. Nursing Science', 'B.NSc. Nursing Science'),
        ('B.Sc. Accounting', 'B.Sc. Accounting'),
        ('B.Sc. Banking and Finance', 'B.Sc. Banking and Finance'),
        ('B.Sc. Biochemistry', 'B.Sc. Biochemistry'),
        ('B.Sc. Biotechnology', 'B.Sc. Biotechnology'),
        ('B.Sc. Business Administration', 'B.Sc. Business Administration'),
        ('B.Sc. Chemistry', 'B.Sc. Chemistry'),
        ('B.Sc. Computer Science', 'B.Sc. Computer Science'),
        ('B.Sc. Cyber Security', 'B.Sc. Cyber Security'),
        ('B.Sc. Economics', 'B.Sc. Economics'),
        ('B.Sc. Fisheries & Aquaculture', 'B.Sc. Fisheries & Aquaculture'),
        ('B.Sc. Information Technology', 'B.Sc. Information Technology'),
        ('B.Sc. Mass Communication', 'B.Sc. Mass Communication'),
        ('B.Sc. Mathematics', 'B.Sc. Mathematics'),
        ('B.Sc. Microbiology', 'B.Sc. Microbiology'),
        ('B.Sc. Physics', 'B.Sc. Physics'),
        ('B.Sc. Political Science', 'B.Sc. Political Science'),
        ('B.Sc. Software Engineering', 'B.Sc. Software Engineering'),
    ]

    programme = SelectField('Select Your Degree:', choices=degrees, validators=[DataRequired()], default='')
    level = StringField('Level', validators=[DataRequired(), Length(max=3)])
    submit = SubmitField('Login')
