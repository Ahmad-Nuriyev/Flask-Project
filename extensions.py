from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

from app import app

csrf = CSRFProtect(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)
migrate = Migrate (app, db)
admin = Admin(app, name = "EShopper", template_mode='bootstrap3')

