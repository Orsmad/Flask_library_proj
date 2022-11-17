from flask_sqlalchemy import SQLAlchemy
from flask import Flask 


app = Flask(__name__)

##########################################
############ DATABASE SETUP ##############
##########################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite3'
app.config['SECRET_KEY'] = "secret_key"
db = SQLAlchemy(app)


##########################################
########## BLUEPRINTS REGISTER ########### 
##########################################

from project.core.views import core
from project.books.views import books
from project.customers.views import customers
from project.loans.views import loans

app.register_blueprint(books)
app.register_blueprint(customers)
app.register_blueprint(loans)
app.register_blueprint(core)


