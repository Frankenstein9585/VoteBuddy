from flask_login import current_user, login_user, logout_user, login_required
from config import app, bcrypt
from flask import flash, render_template, redirect, url_for, request
from admin.forms import AdminRegisterForm, AdminLoginForm
from models.admin import Admin
from models import Candidate, CandidatePositionAssociation, Positions, User


@app.route('/admin/register', methods=['GET', 'POST'])
# @login_required
def admin_register():
    if current_user.is_authenticated:
        return redirect((url_for('admin.index')))
    form = AdminRegisterForm()
    if form.validate_on_submit():
        if not isinstance(current_user, Admin):
            return 'Error'
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        admin = Admin(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data,
                      password=hashed_password)
        admin.save()
        flash('Registration Successful. You can now login', 'success')
        return redirect(url_for('admin_login'))
    return render_template('admin/register_admin.html', form=form)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.find_obj_by(username=form.username.data)
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            next_page = request.args.get('next')
            flash('Login Successful', 'success')
            return redirect(next_page) if next_page else redirect(url_for('admin.index'))
        else:
            flash('Login Unsuccessful. Check your details and try again', 'danger')
    return render_template('admin/login_admin.html', form=form)


@app.route('/admin/analytics')
@login_required
def result():
    if not isinstance(current_user, Admin):
        return 'You should not be here'
    users_voted_count = len(User.query.filter_by(has_voted=True).all())
    positions = Positions.query.order_by(Positions.index).all()
    return render_template('admin/analytics.html', positions=positions, Candidate=Candidate,
                           CandidatePositionAssociation=CandidatePositionAssociation,
                           users_voted_count=users_voted_count)


@app.route('/admin/logout')
def admin_logout():
    if not isinstance(current_user, Admin):
        return 'You should not be here'
    logout_user()
    return redirect(url_for('admin_login'))
