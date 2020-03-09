from flask_wtf import FlaskForm
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
    status=SelectField("Enquiry Status:",[DataRequired()],choices=[('Pending','Pending'),('Interested','Interested'),('Not Interested','Not Interested'),('Exam Passed','Exam Passed'),('Exam Failed','Exam Failed')])
    submit=SubmitField("Submit")

class UpdateDataForm(FlaskForm):
    name=StringField("Name:",validators=[DataRequired()])
    phone_number=IntegerField("Mobile Number:",validators=[DataRequired()])
    email=EmailField("Email:",validators=[validators.DataRequired(),validators.Email()])
    passout_year=IntegerField("Year of Passout:",validators=[DataRequired()])
    qualification=SelectField("Courses:",[DataRequired()],choices=[('Python','Python'),('Java','Java'),('Javascript','Javascript'),('Propel .NET','Propel >NET')
    course=SelectField("Qualification:",[DataRequired()],choices=[('Btech','Btech'),('Mtech','Mtech'),('MCA','MCA'),('BCA','BCA')])
    place=StringField("Place:",validators=[DataRequired()])
    status=SelectField("Enquiry Status:",[DataRequired()],choices=[('Pending','Pending'),('Interested','Interested'),('Not Interested','Not Interested'),('Exam Passed','Exam Passed'),('Exam Failed','Exam Failed')])
    submit=SubmitField("Submit")

class EnquirySearchForm(FlaskForm):
    e_type=RadioField("Type:",validators=[DataRequired(message="Please select an option")],choices=[('Enquiry Id','Enquiry Id'),('Name','Name'),('Phone','Phone'),('Status','Status')])
    e_name=StringField("Search:",validators=[DataRequired(message="Enter Your Name")])
    submit=SubmitField("Search")


