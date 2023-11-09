from flask_login import current_user, login_user, logout_user

from app import app, bcrypt
from flask import flash, render_template, redirect, request, url_for
from forms.login import LoginForm
from models.user import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for(''))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_obj_by(matric_number=form.matric_number.data)
        if user and bcrypt.check_password_hash(user.password, form.password):
            login_user(user)
            next_page = request.args.get('next')
            flash('Login Successful', 'success')
            return redirect(next_page) if next_page else redirect(url_for(''))
        else:
            flash('Login Unsuccessful. Check your details and try again', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(''))
