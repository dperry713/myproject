from flask import render_template, request, redirect, url_for
from app import db
from app.models import Customer
from app.customers import bp

@bp.route('/')
def list_customers():
    customers = Customer.query.all()
    return render_template('customers/list.html', customers=customers)

@bp.route('/create', methods=['GET', 'POST'])
def create_customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        new_customer = Customer(name=name, email=email, phone=phone)
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('customers.list_customers'))
    return render_template('customers/create.html')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    if request.method == 'POST':
        customer.name = request.form['name']
        customer.email = request.form['email']
        customer.phone = request.form['phone']
        db.session.commit()
        return redirect(url_for('customers.list_customers'))
    return render_template('customers/update.html', customer=customer)

@bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(customer)
        db.session.commit()
        return redirect(url_for('customers.list_customers'))
    return render_template('customers/delete.html', customer=customer)
