
from flask import request, render_template, Blueprint, redirect, url_for, flash
from project import db
from project.books.models import Books





books = Blueprint('books', __name__, template_folder='templates')



@books.route("/all_books/<ind>", methods = ['GET'])
@books.route("/all_books/", methods = ['GET'])
# shows all books by default , shows a book by id - as a parameter
def show_books(ind =-1): 
    book_searched=Books.query.get(int(ind))
    if int(ind) > -1  and book_searched != None:
        return render_template("book.html", book=book_searched)
    return render_template("books.html", books=Books.query.filter_by(is_active = True))
   
  
@books.route("/add_book/", methods=['POST','GET'])
# adds a new book.
def add_book():   
    if request.method == 'POST':
        name = request.form.get("name")
        author = request.form.get("author")
        year_published =  request.form.get("year_published")
        book_type = request.form.get("book_type")
        book_to_add = Books(name,author,year_published,book_type)
        db.session.add (book_to_add)
        db.session.commit()
        flash("Book added!")
        return redirect(url_for('books.show_books') )
    return render_template("add_book_form.html")

   
@books.route("/delete_book/<ind>", methods=['DELETE', "GET"])
#  deletes a book to the user, gets a book id as a parameter
#  changes db column to active = false, acts as a delete function
def delete_book(ind=-1): 
    Book_to_delete=Books.query.get(int(ind))
    Book_to_delete.is_active = False
    db.session.commit()
    flash("Book deleted!")
    return redirect(url_for('books.show_books') )   


@books.route("/search_book/", methods=['GET','POST'])
# search a book by name, gets a name from a form
def search_book():
    if request.method == 'POST':
        books = Books.query.filter_by(is_active = True)
        for book in books:
            if request.form.get("name") == book.name:
                return redirect(url_for('books.show_books', ind =book.id))
    flash("Book not found!")
    return redirect(url_for('books.show_books') )   

