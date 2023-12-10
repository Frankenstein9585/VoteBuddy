def check_id(img_path, matric_number):
    from config import User
    from gcloud_ocr import detect_text
    student_info = detect_text(img_path)
    if not student_info:
        return None
    if 'Student Identification Card' in student_info:
        if matric_number in student_info:
            user = User.find_obj_by(matric_number=matric_number)
            if user:
                return user
        return None
