from flask import url_for, redirect, render_template, request, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

from app import app
from models import User, Product, Contact, Category, Images
from forms import RegisterForm, LoginForm, ContactForm

@app.route('/')
@app.route ('/shop/')
def shop():
    category = Category.query.all()
    products = Product.query.all()

    context = {
        'category' : category,
        'products' : products
    }
    return render_template ('shop.html', **context)


@app.route ('/shop/<int:id>/')
def detail(id):
    details = Product.query.get(id)
    images = Images.query.filter_by(product_id=id).all()

    context = {
        'details' : details,
        'images' : images
    }
    return render_template ('detail.html', **context)

# Endirim qiymətləri mövcud olan məhsullar üçün ayrı səhifə
@app.route ('/discounted/')
def discount():
    products = Product.query.filter(Product.discount_price != None).all()    
    return render_template ('discount.html', products=products)


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
             user.save()
             flash ("Successful registration", 'success')
             return redirect (url_for('login'))
        flash ("Incorrect data in fields", 'danger') 
    return render_template ('register.html', form=form)

        
# Login səhifəsi üçün kod
@app.route ('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            user = User.query.filter_by(email=email).first()

            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash ('Login successful', 'success')
                return redirect(url_for('shop'))
        flash ('Mail or password are incorrect', 'danger')

    return render_template ('login.html', form=form)


# Contact səhifəsi üçün kod
@app.route ('/contact/', methods = ['GET', 'POST'])
def contacts():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            contact = Contact(                
                name = form.name.data,
                email = form.email.data,
                subject = form.subject.data,
                message = form.message.data
            )
            contact.save()
            flash ("Thank you for contacting us", 'success')
            return redirect(url_for('contacts'))
        flash ("Some field(s) remain empty", 'danger')
            
    return render_template ('contact.html', form=form)
