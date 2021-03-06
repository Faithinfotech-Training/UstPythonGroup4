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
    mobile=IntegerField("MOBILE :",validators=[DataRequired()])
    email=StringField("EMAIL:",validators=[DataRequired(),Email()])
    role_id=RadioField('', choices = [('1','admin'),('2','cordinator')],validators=[DataRequired()])
    username=StringField("USERNAME: ",validators=[validators.required(), validators.Length(min=2, max=35)])
    password=PasswordField("PASSWORD: ",validators=[validators.required(), validators.Length(min=2, max=35)])
    password2=PasswordField("REPEAT PASSWORD: ",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("REGISTER")
    
from wtforms import StringField,IntegerField,PasswordField,BooleanField,SubmitField,RadioField,SelectField,TextAreaField
from wtforms.validators import DataRequired,EqualTo,ValidationError,Email
from wtforms.fields.html5 import EmailField
from wtforms import validators

class EnquiryForm(FlaskForm):
    name=StringField("Name:",validators=[DataRequired()])
    phone_number=IntegerField("Mobile Number:",validators=[DataRequired()])
    email=EmailField("Email:",validators=[validators.DataRequired(),validators.Email()])
    passout_year=IntegerField("Year of Passout:",validators=[DataRequired()])
    qualification=SelectField("Qualification:",[DataRequired()],choices=[('Btech','Btech'),('Mtech','Mtech'),('MCA','MCA'),('BCA','BCA')])
    course=SelectField("Courses:",[DataRequired()],choices=[('Python','Python'),('Java','Java'),('Javascript','Javascript'),('Propel .NET','Propel >NET')])
    place=StringField("Place:",validators=[DataRequired()])
    status=SelectField("Enquiry Status:",[DataRequired()],choices=[('Pending','Pending'),('Interested','Interested'),('Not Interested','Not Interested'),('Exam Passed','Exam Passed'),('Exam Failed','Exam Failed'),('Exam Joined','Exam Joined')])
    submit=SubmitField("Submit")

class UpdateDataForm(FlaskForm):
    name=StringField("Name:",validators=[DataRequired()])
    phone_number=IntegerField("Mobile Number:",validators=[DataRequired()])
    email=EmailField("Email:",validators=[validators.DataRequired(),validators.Email()])
    passout_year=IntegerField("Year of Passout:",validators=[DataRequired()])
    course=SelectField("Courses:",[DataRequired()],choices=[('Btech','Btech'),('Mtech','Mtech'),('MCA','MCA'),('BCA','BCA')])
    qualification=SelectField("Qualification:",[DataRequired()],choices=[('Python','Python'),('Java','Java'),('Javascript','Javascript'),('Propel .NET','Propel >NET')])
    place=StringField("Place:",validators=[DataRequired()])
    status=SelectField("Enquiry Status:",[DataRequired()],choices=[('Pending','Pending'),('Interested','Interested'),('Not Interested','Not Interested'),('Exam Passed','Exam Passed'),('Exam Failed','Exam Failed'),('Exam Joined','Exam Joined')])
    submit=SubmitField("Submit")

class EnquirySearchForm(FlaskForm):
    e_type=RadioField("Type:",validators=[DataRequired(message="Please select an option")],choices=[('Enquiry Id','Enquiry Id'),('Name','Name'),('Phone','Phone'),('Status','Status')])
    e_name=StringField("Search:",validators=[DataRequired(message="Enter Your Name")])
    submit=SubmitField("Search")


