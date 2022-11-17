from project import db, app

# loans model- creates a loans table

class Loans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'),nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'),nullable=False)
    loan_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date,  default=None)

    def __init__(self, customer_id, book_id, loan_date,return_date = None ):
        self.customer_id=customer_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date


with app.app_context():
    db.create_all()