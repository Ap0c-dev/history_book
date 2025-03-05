import os
from flask import Flask
from app.models import db

DB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data', 'data_history_book.sqlite')

def create_app():
    app = Flask(__name__)

    if not os.path.exists(os.path.dirname(DB_PATH)):
        os.makedirs(os.path.dirname(DB_PATH))

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24).hex()  

    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("Banco de dados criado!")

    return app
