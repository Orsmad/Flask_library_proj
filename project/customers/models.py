from project import db, app

# customers model- creates a customers table
class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, unique=False, default=True)
    loans = db.relationship('Loans', backref='customers')


    def __init__(self, name, city, age):
        self.name=name
        self.city = city
        self.age = age
        self.is_active = True



with app.app_context():
    db.create_all()