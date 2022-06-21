import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with open('/Users/wojciechziarnik/Desktop/DEV/FlaskCourseFCC/market/secret_key.json') as secret_file:
    secret_key = json.load(secret_file)

app.config['SECRET_KEY'] = secret_key['SECRET_KEY']

bcrypt = Bcrypt(app)

from market import routes
