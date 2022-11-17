
from project import db, app
from project.books.models import Books
from project.customers.models import Customers
from project.loans.models import Loans
from datetime import date

# run this file to populate

# adds 3 books - 3 diffrent book type
book1 = Books(year_published= 1998,   name = "it",author ="stephen king",type = 1)
book2 = Books(year_published= 2019,   name = "salems lot",author ="stephen king",type=2)
book3 = Books(year_published= 1935,   name = "brave new world",author ="huxly",type=3)

# adds 3 customers
customer1= Customers(name = "joe", city = "tel-aviv", age= 31)
customer2= Customers(name = "david", city = "lod-aviv", age= 23)
customer3= Customers(name = "james", city = "lod-angeles", age= 18)

#  adds 3 loans- 2 late loans and 1 returned 
loan1 = Loans(customer_id= 1, book_id =1 , loan_date=date(2022, 10, 10) )
loan2 = Loans(customer_id= 2, book_id =2 , loan_date=date(2022, 10, 20))
loan3 = Loans(customer_id= 3, book_id =3 , loan_date=date(2022, 10, 10 ), return_date = date(2022, 10, 11))




with app.app_context():

    db.session.add_all([book1, book2,book3])
    db.session.add_all([customer1, customer2 ,customer3 ])
    db.session.add_all([loan1, loan2,loan3])


    db.session.commit()

