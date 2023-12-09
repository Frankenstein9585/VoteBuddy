from config import User, app
from gcloud_ocr import detect_text


# with app.app_context():
#     students = User.query.all()
#
# matric_numbers = [student.matric_number for student in students]
# print(matric_numbers)
def check_id(img_path, matric_number):
    student_info = detect_text(img_path)
    if 'Student Identification Card' in student_info:
        if matric_number in student_info:
            user = User.find_obj_by(matric_number=matric_number)
            if user:
                return user
        return None
    return False
