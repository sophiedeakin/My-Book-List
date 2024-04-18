from flask import Flask, render_template, request, redirect,  url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(50))
    comments = db.Column(db.String(200))
    status = db.Column(db.String(10))


@app.route('/')
def index():
    books = Book.query.all()   
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
        title = request.form['title']
        author = request.form['author']
        comments = request.form['comments']
        status = request.form['status']
    
        new_book = Book(title=title, author=author, comments=comments, status=status)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    book = Book.query.get(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.comments = request.form['comments']
        book.status = request.form['status']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', book=book)

@app.route('/delete/<int:id>')
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
         db.create_all()
    app.run(debug=True)