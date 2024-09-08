from flask import url_for, redirect, render_template, request, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

from app import app
from extensions import db
from models import User, Product
from forms import RegisterForm, LoginForm

@app.route('/')
@app.route ('/shop/')
def shop():
    return render_template ('shop.html')

@app.route ('/products/') #('/products/<int:id>/')
def product():
    return render_template ('detail.html')

@app.route ('/favourites/', methods = ['GET', 'POST'])
def favourite():
    return render_template ('favorites.html')

# Registrasiya səhifəsi üçün kod
@app.route ('/register/', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == "POST":          
        if form.validate_on_submit():
             user = User(
                  name = form.name.data,
                  surname = form.surname.data,
                  email = form.email.data,
                  password = form.password.data,                    
             )
             print (form.data)
             user.save()
             flash ("Successful registration", 'success')
             return redirect (url_for('login'))
        flash ("Incorrect data in fields", 'danger') 
    return render_template ('register.html', form=form)

        
# Login səhifəsi üçün kod
@app.route ('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            user = User.query.filter_by(email=email).first()

            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash ('Login successful', 'success')
        flash ('Mail or password are incorrect', 'danger')

    return render_template ('login.html', form=form)

@app.route ('/contact/')
def contacts():
    return render_template ('contact.html')
