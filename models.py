from extensions import db


class User (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.String(50), nullable = False)
    surname = db.Column (db.String(50), nullable = False)
    email = db.Column (db.Text, nullable = False)
    password = db.Column (db.Text, nullable = False)

    # created_at = db.Column (db.Datetime, server_default = db.func.now())
    # updated_at = db.Column (db.Datetime, server_default = db.funk.now(), server_onupdate = db.func.now())


class Product (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.String(50), nullable = False)
    price = db.Column (db.Integer, nullable = False)
    discount_price = db.Column (db.Integer, nullable = False)
    photo = db.Column (db.Text, nullable = False)

    # created_at = db.Column (db.Datetime, server_default = db.func.now())
    # updated_at = db.Column (db.Datetime, server_default = db.funk.now(), server_onupdate = db.func.now())