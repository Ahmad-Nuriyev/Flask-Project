from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from models import User

def password_check(form, field):
    password = field.data
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least one digit.")
    
    # Check for at least one of the symbols #, $, or %
    if not any(char in '#$%' for char in password):
        raise ValidationError("Password must contain at least one special character (#, $, or %).")
    
def email_check(form, field):
    user = User.query.filter_by(email=field.data).first()
    if user is not None:
        raise ValidationError("Mail is already used")

class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), email_check])
    password = PasswordField('Password', validators=[DataRequired(), password_check])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo("password", message="Passwords are not identical")])
    
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = EmailField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')
