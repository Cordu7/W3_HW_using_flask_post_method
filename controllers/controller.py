from flask import render_template,request,redirect
from app import app
from models.book_list import book_list, add_new_book, delete_book
from models.book_class import Book
import datetime

@app.route('/books')
def index():
    return render_template('index.html', title='Home', book_list=book_list)

@app.route('/books/<index>')
def view_book(index):
    book_to_view= book_list[int(index)-1]
    return render_template('books.html', title= "View Book", book=book_to_view )

@app.route('/books', methods= ['POST'])
def add_book():
    title= request.form['title']
    author=request.form['author']
    genre=request.form['genre']
    date_borrowed=request.form['date']
    split_date = date_borrowed.split('-')
    date_borrowed = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    new_book= Book(title=title, author=author, genre=genre, date_borrowed=date_borrowed)
    add_new_book(new_book)
    return redirect ('/books')

    
  # I dont get why I dont need to reverse the order
  

@app.route('/books/delete/<title>', methods= ['POST'])
def delete(title):
    delete_book(title)
    return redirect ('/books')


