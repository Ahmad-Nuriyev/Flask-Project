from flask import url_for, redirect, render_template

from app import app
from extensions import db


@app.route ('/shop/')
def shop():
    return render_template ('shop.html')

@app.route ('/products/<int:id>/')
def product():
    return render_template ('detail.html')

@app.route ('/favourites/', methods = ['GET', 'POST'])
def favourite():
    return render_template ('favorites.html')

@app.route ('/register/')
def register():
    return render_template ('register.html')

@app.route ('/login/')
def login():
    return render_template ('login.html')

@app.route ('/contact/')
def contacts():
    return render_template ('contact.html')
