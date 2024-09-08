from extensions import db, login_manager
from werkzeug.security import generate_password_hash


class User (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.String(50), nullable = False)
    surname = db.Column (db.String(50), nullable = False)
    email = db.Column (db.Text, nullable = False)
    password = db.Column (db.Text, nullable = False)

    product_id = db.relationship('Product', secondary = 'user_products')
 
    created_at = db.Column (db.DateTime, server_default = db.func.now())
    updated_at = db.Column (db.DateTime, server_default = db.func.now(), server_onupdate = db.func.now())

    def __repr__(self):
        return f"<{self.name}>"
    
    @property
    def full_name(self):
        return f"{self.name} {self.surname}"
    
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
    price = db.Column (db.Integer, nullable = False)
    discount_price = db.Column (db.Integer, nullable = False)
    photo = db.Column (db.Text, nullable = False)

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
