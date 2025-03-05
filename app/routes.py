from flask import Flask, app, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app.models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/data_history_book.sqlite'

db.init_app(app)

def config_routes(app):
    @app.route('/')
    def index():
        books = Book.query.all()
        return render_template('index.html', books=books)
    
    @app.route('/add_book', methods=['GET', 'POST'])
    def add_book():
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            year = request.form['year']
            read = 'read' in request.form
            
            new_book = Book(title=title, author=author, year=year, read=read)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('index'))
        
        return render_template('add_book.html')    
    
if __name__ == '__main__':
    app.run(debug=True)  