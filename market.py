from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)  # type: ignore
    name = db.Column(db.String(length=30), nullable=False, unique=True)  # type: ignore
    price = db.Column(db.Integer(), nullable=False)  # type: ignore
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)  # type: ignore
    description = db.Column(db.String(length=1024), nullable=False, unique=True)  # type: ignore


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)
