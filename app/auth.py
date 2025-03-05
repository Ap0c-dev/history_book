from app.models import db, Book, User
from flask import request, current_app as app, Blueprint, session, flash, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(name=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for('books.index'))
        else:
            flash("Usuário ou senha inválidos!", "danger")
            
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Você saiu da conta!", "info")
    return redirect(url_for('auth.login'))
