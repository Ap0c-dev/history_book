from app.models import db, User
from flask import request, current_app as app, Blueprint, session, flash, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

auth = Blueprint('auth', __name__)

@auth.route('register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        date_of_birth = request.form['date_of_birth']
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Usuário já existe!', 'danger')
            return redirect(url_for('auth.register'))
        
        if password != confirm_password:
            flash('As senhas não coincidem!', 'danger')
            return redirect(url_for('auth.register'))
        
        new_user = User(username=username, date_of_birth=date_of_birth)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for('index'))
        else:
            flash("Usuário ou senha inválidos!", "danger")
            return redirect(url_for('index'))
            
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Você saiu da conta!", "info")
    return redirect(url_for('auth.login'))
