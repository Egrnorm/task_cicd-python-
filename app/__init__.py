from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, template_folder='site')
    app.config['SECRET_KEY'] = 'upupuch'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #Путь к базе данных

    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        from . import routes  #Импортируем маршруты (страницы)
        db.create_all()  #Создаём таблицы в базе данных

    return app