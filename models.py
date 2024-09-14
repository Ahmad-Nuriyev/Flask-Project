from extensions import db, login_manager
from werkzeug.security import generate_password_hash
from flask_login import UserMixin


class User (db.Model, UserMixin):
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.String(50), nullable = False)
    surname = db.Column (db.String(50), nullable = False)
    email = db.Column (db.Text, nullable = False)
    password = db.Column (db.Text, nullable = False)

    favorite_products = db.relationship('Product', secondary = 'user_products')
 
    created_at = db.Column (db.DateTime, server_default = db.func.now())
    updated_at = db.Column (db.DateTime, server_default = db.func.now(), server_onupdate = db.func.now())

    def __repr__(self):
        return f"<{self.name}>"
    
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = generate_password_hash(password)
        
    def save(self):
        db.session.add(self)
        db.session.commit()


user_products = db.Table (
    'user_products',
    db.Column ('user.id', db.Integer, db.ForeignKey('user.id')),
    db.Column ('product.id', db.Integer, db.ForeignKey('product.id'))
)


class Product (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.String(50), nullable = False)
    price = db.Column (db.Float, nullable = False)
    discount_price = db.Column (db.Float)
    photo = db.Column (db.Text)
    description = db.Column (db.Text, nullable=False)
    category_id = db.Column (db.Integer, db.ForeignKey('category.id'), nullable=False)

    category = db.relationship ('Category', backref = db.backref('products', uselist=True))

    created_at = db.Column (db.DateTime, server_default = db.func.now())
    updated_at = db.Column (db.DateTime, server_default = db.func.now(), server_onupdate = db.func.now())

    def __repr__(self):
        return f"<{self.name}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Images(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    photo = db.Column (db.Text)
    product_id = db.Column (db.Integer, db.ForeignKey('product.id'))

    products = db.relationship ('Product', backref = db.backref('images', uselist=True, lazy=True))

class Category (db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(50), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    
    parent = db.relationship('Category', remote_side=[id], backref=db.backref('children', uselist=True))
    
    created_at = db.Column (db.DateTime, server_default = db.func.now())
    updated_at = db.Column (db.DateTime, server_default = db.func.now(), server_onupdate = db.func.now())

    def _repr_(self):
        return f"<{self.name}>"


class Contact(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(50), nullable=False)
    email = db.Column (db.Text, nullable=False)
    subject = db.Column (db.String(100), nullable=False)
    message = db.Column (db.Text, nullable=False) 

    created_at = db.Column (db.DateTime, server_default = db.func.now())
    updated_at = db.Column (db.DateTime, server_default = db.func.now(), server_onupdate = db.func.now())

    def __repr__(self):
        return f"<{self.title}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Reviews (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    text = db.Column (db.Text, nullable=False)
    user_id = db.Column (db.Integer, db.ForeignKey ('user.id'))
    product_id = db.Column (db.Integer, db.ForeignKey ('product.id'))
    
    users = db.relationship ('User', backref = db.backref('reviews', uselist=True))
    products = db.relationship ('Product', backref = db.backref('prodreview', uselist=True))
    
    created_at = db.Column (db.DateTime, server_default = db.func.now())
    updated_at = db.Column (db.DateTime, server_default = db.func.now(), server_onupdate = db.func.now())

    def __repr__(self):
        return f"<{self.title}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
