from flask_login import current_user, login_user, logout_user

from config import app, bcrypt
from flask import flash, render_template, redirect, request, url_for
from forms.login import LoginForm
from models.user import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_obj_by(matric_number=form.matric_number.data)
        if user and user.has_registered:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                next_page = request.args.get('next')
                flash('Login Successful. Click your name for more info', 'success')
                return redirect(next_page) if next_page else redirect(url_for('index'))
            else:
                flash('Login Unsuccessful. Check your details and try again', 'danger')
        else:
            flash('Login Unsuccessful. Make sure you register before logging in', 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
