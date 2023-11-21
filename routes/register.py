from flask_login import current_user

from config import app, bcrypt
from flask import flash, render_template, redirect, url_for
from forms.register import RegisterForm
from models.user import User


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                    matric_number=form.matric_number.data, password=hashed_password)
        user.save()
        flash('Registration Successful. You can now Login', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)
