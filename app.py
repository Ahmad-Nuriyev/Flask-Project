from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:ProjectFlask@localhost:3306/FlaskProject"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config["SECRET_KEY"] = '6ba0fdb3b26c8a06204f5a4538392463'


from controllers import *
from models import *
from extensions import *


if __name__ == '__main__':
    from admin import *
    app.run(debug=True, port= 8000)