from config import User, app
from gcloud_ocr import detect_text

with app.app_context():
    matric_numbers = User.query.all()

print(matric_numbers)
def check_id(img_path):
    student_info = detect_text(img_path)
