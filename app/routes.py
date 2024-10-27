from flask import request, render_template, redirect, url_for, flash, make_response
from . import db
from .models import User
from flask import current_app as app
import jwt  # Библиотека для работы с токенами
from datetime import datetime, timedelta, timezone  # Для работы со временем

def generate_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=30)  # Токен действует 30 минут
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token


def check_token():
    token = request.cookies.get('token')  #Получаем токен из cookie
    if not token:
        flash('Требуется аутентификация. Пожалуйста войдите')
        return False

    try:
        jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return True
    except jwt.ExpiredSignatureError:
        flash('Ваша сессия истекла. Пожалуйста войдите снова')
    except jwt.InvalidTokenError:
        flash('Неверный токен. Попробуйте ещё раз')

    return False

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Пользователь с таким именем уже существует')
            return redirect(url_for('register'))
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            flash('Неверный логин или пароль')
            return redirect(url_for('login'))


        token = generate_token(user)
        response = make_response(redirect(url_for('main')))
        response.set_cookie('token', token)
        return response

    return render_template('login.html')

@app.route('/main')
def main():
    if not check_token():
        return redirect(url_for('login'))
    return render_template('main.html')


@app.route('/healthz')
def healthz():
    return render_template('healthz.html')