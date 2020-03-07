from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField , IntegerField ,RadioField
from wtforms import validators
from wtforms.validators import Email
from wtforms.validators import DataRequired, EqualTo, ValidationError
from wtforms.fields.html5 import EmailField
from app_package.models import Role,Login,Registration

class LoginForm(FlaskForm):
    username=StringField("Username: ",validators=[validators.required(), validators.Length(min=2, max=35)])
    password=PasswordField("Password: ",validators=[validators.required(), validators.Length(min=2, max=35)])
    remember_me=BooleanField("Remember Me")
    submit=SubmitField("Sign in")
    


class RegistrationForm(FlaskForm):
    fullname=StringField("FULLNAME: ",validators=[validators.required(), validators.Length(min=2, max=35)])
    username=StringField("USERNAME: ",validators=[validators.required(), validators.Length(min=2, max=35)])
    mobile=IntegerField("MOBILE :",validators=[DataRequired()])
    email=StringField("Email:",validators=[DataRequired(),Email()])
    role_id=RadioField('', choices = [('1','admin'),('2','cordinator')],validators=[DataRequired()])
    password=PasswordField("PASSWORD: ",validators=[validators.required(), validators.Length(min=2, max=35)])
    password2=PasswordField("REPEAT PASSWORD: ",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("REGISTER")
    