from project import db, app

# books model- creates a books table
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean,name="is_active", unique=False, default=True)

    loans = db.relationship('Loans', backref='books')
  

    def __init__(self, name, author, year_published, type):
        self.name = name
        self.author= author
        self.year_published=year_published
        self.type=type
        self.is_active = True

with app.app_context():
    db.create_all()