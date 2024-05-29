def check_id(img_path, matric_number):
    from config import User
    from utils.aws_ocr import aws_textract_local
    student_info = aws_textract_local(img_path)
    print(student_info)
    if not student_info:
        return None
    if 'Student Identification Card'.casefold() in student_info:
        if matric_number.casefold() in student_info:
            user = User.find_obj_by(matric_number=matric_number)
            if user:
                return user
        return None
