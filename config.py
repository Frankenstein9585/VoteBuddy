from os import getenv

from flask import Flask, session, jsonify
from flask_admin import Admin
from admin.admin import UserView, MyAdminIndexView, PositionsView, VoteView, CandidateView
from flask_babel import Babel
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect, generate_csrf
import logging

user = getenv('VOTEBUDDY_USER')
password = getenv('VOTEBUDDY_PWD')
database = getenv('VOTEBUDDY_DB')
host = getenv('VOTEBUDDY_HOST')

app = Flask(__name__)

app.config['SECRET_KEY'] = '2418a51bfc930c04eac5d264b84806c6'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{password}@{host}/{database}'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'category'
migrate = Migrate(app, db)

csrf = CSRFProtect(app)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

babel = Babel(app)
admin = Admin(app, index_view=MyAdminIndexView())

from models import Admin, Candidate, User, Vote, Positions

admin.add_view(UserView(User, db.session))
admin.add_view(CandidateView(Candidate, db.session))
admin.add_view(VoteView(Vote, db.session))
admin.add_view(PositionsView(Positions, db.session))


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(str(user_id))
    if user:
        return user
    admin = Admin.query.get(str(user_id))
    return admin


@app.route('/token')
def token():
    csrf_token = generate_csrf()
    session['csrf_token'] = csrf_token
    session.modified = True
    return jsonify({'X-CSRFToken': csrf_token})


from routes import index, login, register
from admin.routes import admin_login, admin_register
