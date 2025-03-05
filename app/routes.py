from flask import Flask, app, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from app.models import User, db, Book
from app.auth import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/data_history_book.sqlite'

db.init_app(app)

app.register_blueprint(auth, url_prefix='/auth')

def config_routes(app):
    @app.route('/')
    def login():
        return render_template('login.html')
    
    @app.route('/register')
    def register():
        return render_template('register.html')
    
    @app.route('/index')
    def index():
        if 'user_id' not in session:
            flash('Você precisa estar logado para ver os livros', 'danger')
            return redirect(url_for('auth.login'))
        
        user_id = session['user_id']
        books = Book.query.filter_by(user_id=user_id).all()
        
        return render_template('index.html', books=books)
    
    @app.route('/add_book', methods=['GET', 'POST'])
    def add_book():
        if 'user_id' not in session:
            flash('Você precisa estar logado para adicionar um livro', 'danger')
            return redirect(url_for('auth.login'))
        
        user_id = session['user_id']
        
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            year = request.form['year']
            read = 'read' in request.form
            
            new_book = Book(title=title, author=author, year=year, read=read, user_id=user_id)
            db.session.add(new_book)
            db.session.commit()
            flash('Livro adicionado com sucesso!', 'success')
            return redirect(url_for('index'))
        
        return render_template('add_book.html')    
    
if __name__ == '__main__':
    app.run(debug=True)  