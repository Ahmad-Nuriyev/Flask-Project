from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from models import User

def password_check(form, field):
    password = field.data
    
    # bir böyük hərfin olmasını yoxlayır
    if not any(char.isupper() for char in password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    
    # ən azı bir kiçik hərfin olmasını yoxlayır
    if not any(char.islower() for char in password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    
    # ən azı bir rəqəmin olmağını yoxlayır
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least one digit.")
    
    # #, $, vəya % simvolların olmasını yoxlayır
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


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])

    submit = SubmitField('Send Message')


class ReviewForm(FlaskForm):
    text = TextAreaField('Your Review', validators=[DataRequired()])

    submit = SubmitField()
