
from flask import request, render_template, Blueprint, redirect, url_for, flash
from project.customers.models import Customers
from project import db


customers = Blueprint('customers', __name__, template_folder='templates')


@customers.route("/all_customers/<ind>", methods = ['GET'])
@customers.route("/all_customers/" , methods = ['GET'])
# shows all customers by default , shows a customer by id - as a parameter
def show_customers(ind =-1): 
    customer_searched=Customers.query.get(int(ind))
    if int(ind) > -1 and customer_searched != None:
        return render_template ("customer.html",customer=customer_searched)
    return render_template ("customers.html", customers=Customers.query.filter_by(is_active = True))

    
  
@customers.route("/add_customer/", methods=['POST','GET'])
# adds a new customer 
def add_customer():
    if request.method == 'POST':
        name = request.form.get("name")
        city = request.form.get ("city")
        age = request.form.get ("age")
        customer_to_add = Customers(name, city, age)
        db.session.add (customer_to_add)
        db.session.commit()
        flash("customer added!")
        return redirect(url_for('customers.show_customers'))
    return render_template("add_customer_form.html")
 

@customers.route("/delete_customer/<ind>", methods=['GET'])
# deletes a customer, gets a customer id as a parameter.
# changes db column to active = false, acts as a delete function
def delete_customer(ind=-1): 
    customer_to_delete=Customers.query.get(int(ind))
    customer_to_delete.is_active = False
    db.session.commit()
    flash("customer deleted!")
    return redirect(url_for('customers.show_customers'))



@customers.route("/search_customer/", methods=['GET', 'POST'])
# search a customer by name, gets a name from a form
def search_customer():
    if request.method == 'POST':
        customers = Customers.query.filter_by(is_active = True)
        for customer in customers:
            if request.form.get("name") == customer.name:
                return render_template("customer.html", customer=customer) 
    flash("customer not found!")
    return redirect(url_for("customers.show_customers"))


