from os import getenv

from flask import Flask, session, jsonify
from flask_admin import Admin
from admin import ModelView
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
admin = Admin(app)

from models import User

admin.add_view(ModelView(User, db.session))

from routes import index, login, register


@app.route('/token')
def token():
    csrf_token = generate_csrf()
    session['csrf_token'] = csrf_token
    session.modified = True
    return jsonify({'X-CSRFToken': csrf_token})
