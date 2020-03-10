from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,PasswordField,BooleanField,SubmitField,RadioField,SelectField,TextAreaField
from wtforms.validators import DataRequired,EqualTo,ValidationError,Email
from wtforms.fields.html5 import EmailField
from wtforms import validators


class AdmissionSearchForm(FlaskForm):
    e_phone=IntegerField("Phone:",validators=[DataRequired()])
    submit=SubmitField("Search")

class AdmissionAddForm(FlaskForm):
    e_name=StringField("Name:",validators=[DataRequired()])
    e_gender=RadioField("Gender:",choices = [('Male','Male'),('Female','Female'),('Other','Other')])
    e_phone=IntegerField("Phone:",validators=[DataRequired()])
    e_email=StringField("Email:",validators=[DataRequired()])
    e_qualification=StringField("Course Of Interest:",validators=[DataRequired()])
    e_course_of_interest=StringField("Highest Qualification:",validators=[DataRequired()])
    e_year_of_pass=IntegerField("Passout Yaer:",validators=[DataRequired()])
    e_status=RadioField("Status:",choices = [('Joined','Joined')])
    batch_name=SelectField("Batch Assigned:",choices=[],coerce=str)
    e_guardianname=StringField("Gaurdian Name:",validators=[DataRequired()])
    e_guardianphone=IntegerField("Guardian Phone:",validators=[DataRequired()])
    e_address=TextAreaField("Address:")
    submit=SubmitField("Add")

class AdmissionUpdateForm(FlaskForm):
    e_name=StringField("Name:",validators=[DataRequired()])
    e_gender=RadioField("Gender:",choices = [('Male','Male'),('Female','Female'),('Other','Other')])
    e_phone=IntegerField("Phone:",validators=[DataRequired()])
    e_email=StringField("Email:",validators=[DataRequired()])
    e_qualification=StringField("Highest Qualification:",validators=[DataRequired()])
    e_course_of_interest=StringField("Course Of Interest:",validators=[DataRequired()])
    e_year_of_pass=IntegerField("Passout Year:",validators=[DataRequired()])
    e_status=RadioField("Status:",choices = [('Joined','Joined')])
    batch_name=SelectField("Batch Assigned:",choices=[],coerce=str)
    e_guardianname=StringField("Gaurdian Name:",validators=[DataRequired()])
    e_guardianphone=IntegerField("Guardian Phone:",validators=[DataRequired()])
    e_address=TextAreaField("Address:")
    submit=SubmitField("Add")
