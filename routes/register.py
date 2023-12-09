import base64
import io

from flask_login import current_user

from config import app, bcrypt
from flask import flash, render_template, redirect, request, url_for
from forms.register import RegisterForm
from models.user import User
from gcloud_ocr import detect_text
from PIL import Image


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # for key, value in form.data.items():
        #     print(f'{key}: {value}')
        image_bytes = base64.b64decode(form.image_byte_string.data.split(',')[1])
        img = Image.open(io.BytesIO(image_bytes))
        img.save(f"{request.form.get('matric_number')}.png", format='PNG')
        student_info = detect_text(f'{form.matric_number.data}.png')
        print(student_info)
        if form.matric_number.data in student_info:
            print('YES')
        return 'Done'
    return render_template('register.html', form=form)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    # form = RegisterForm()
    # if form.validate_on_submit():
    # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    # user = User(first_name=form.first_name.data, last_name=form.last_name.data,
    #             matric_number=form.matric_number.data, password=hashed_password)
    # user.save()
    # flash('Registration Successful. You can now Login', 'success')
    # return redirect(url_for('index'))
    # for key, value in form.data.items():
    #     print(f'{key}: {value}')
    ...
    captured_image_data: str = request.form.get('capturedImageData')
    print(type(captured_image_data))
    print(captured_image_data)
    image_bytes = base64.b64decode(captured_image_data.split(',')[1])

    img = Image.open(io.BytesIO(image_bytes))

    img.save(f"{request.form.get('matric_number')}.png", format='PNG')

    # image_file = open(f"{request.form.get('matric_number')}.png", 'wb')
    # image_file.write(image_bytes)
    # image_file.close()

    return 'Done'
