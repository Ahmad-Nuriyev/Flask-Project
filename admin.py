from flask_admin.contrib.sqla import ModelView

from extensions import admin, db

from models import Product, Category, Reviews, User, Contact, Images

admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Reviews, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Contact, db.session))
admin.add_view(ModelView(Images, db.session))
