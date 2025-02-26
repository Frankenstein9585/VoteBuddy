# from config import app, db
#
#
# def populate_users():
#     import csv
#     from models import User
#     csv_file_path = '../data/AUI_students_2024_2025.csv'
#     with app.app_context():
#         with open(csv_file_path, 'r') as csv_file:
#             csv_reader = csv.DictReader(csv_file)
#             for row in csv_reader:
#                 new_user = User(**row)
#                 new_user.name = new_user.name.title()
#                 db.session.add(new_user)
#             db.session.commit()
#
#
# populate_users()


print('Donald' in 'Donald Dikachi Peters')

