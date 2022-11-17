from flask import  request, render_template, Blueprint, redirect, url_for, flash
from project.loans.models import Loans
from project.books.models import Books
from datetime import date, datetime
from project import db 



loans = Blueprint('loans', __name__, template_folder='templates')


@loans.route("/all_loans/")
# shows all loans  
def show_loans(): return render_template("loans.html",loans=Loans.query.all()) 

@loans.route("/late_loans/", methods=['GET'])
# shows late loans by type
def late_loans():
    all_loans = Loans.query.filter(Loans.return_date == None)
    late_loans = []
    today= date.today()
    for loan in all_loans:
        book= Books.query.get(loan.book_id)
        delta= today - loan.loan_date
        delta= delta.days
        if book.type == 1 and delta > 10:
            late_loans.append(loan)
        if book.type == 2 and delta > 5:
            late_loans.append(loan)
        if book.type == 3 and delta > 2:
            late_loans.append(loan)
    return  render_template("late_loans.html",loans=late_loans) 


@loans.route("/return_book/<ind>", methods=['POST','GET'])
# return a book/updates return date, gets a return date in form, gets book id in the url
def return_book(ind = -1): 
    if request.method == 'POST' and int(ind) > -1:
        loan=Loans.query.get(int(int(ind)))
        if request.form['return_date'] == '': 
            return_date = None
            return redirect(url_for('loans.show_loans')) 
        else: return_date = datetime.strptime( request.form['return_date'], '%Y-%m-%d')
        loan.return_date = return_date
        db.session.commit()
        flash("book returned!")
        return redirect(url_for('loans.show_loans')) 
    return render_template("return_book_form.html")  

@loans.route("/add_loan/", methods=['POST','GET'])
# adds a new loan /	Loan a book
def add_loan(): 
    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        book_id = request.form.get('book_id')
        loan_date = datetime.strptime( request.form['loan_date'], '%Y-%m-%d')
        if request.form['return_date'] == '': return_date = None
        else: return_date = datetime.strptime( request.form['return_date'], '%Y-%m-%d')
        loan_to_add = Loans(customer_id, book_id, loan_date, return_date )
        db.session.add (loan_to_add)
        db.session.commit()
        flash("Loan added!")
        return redirect(url_for('loans.show_loans'))
    return render_template("add_loan_form.html")   