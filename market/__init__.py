import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with open('/Users/wojciechziarnik/Desktop/DEV/FlaskCourseFCC/market/secret_key.json') as secret_file:
    secret_key = json.load(secret_file)

app.config['SECRET_KEY'] = secret_key['SECRET_KEY']

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = "login_page"

login_manager.login_message_category = "info"

from market import routes
