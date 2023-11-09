from os import getenv

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

user = getenv('VOTEBUDDY_USER')
password = getenv('VOTEBUDDY_PWD')
database = getenv('VOTEBUDDY_DB')
host = getenv('VOTEBUDDY_HOST')

app = Flask(__name__)

app.config['SECRET_KEY'] = '2418a51bfc930c04eac5d264b84806c6'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{password}@{host}/{database}'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
