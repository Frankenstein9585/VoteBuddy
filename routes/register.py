import base64
import io
import os

from flask_login import current_user

from config import app, bcrypt
from flask import flash, render_template, redirect, request, url_for
from forms.register import RegisterForm
# from gcloud_ocr import detect_text
from utils.check_id import check_id
from PIL import Image


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        # for key, value in form.data.items():
        #     print(f'{key}: {value}')
        if not form.image_byte_string:
            flash('Please upload valid Student ID Card', 'danger')
        image_bytes = base64.b64decode(form.image_byte_string.data.split(',')[1])
        img = Image.open(io.BytesIO(image_bytes))
        img.save(f"{request.form.get('matric_number')}.png", format='PNG')
        user = check_id(f'{form.matric_number.data}.png', form.matric_number.data)
        if user:
            user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.has_registered = True
            user.save()
            flash('Registration Successful. You can now login', 'success')
            return redirect(url_for('login'))
        else:
            flash('Please upload valid Student ID Card', 'danger')
    return render_template('register.html', form=form)
