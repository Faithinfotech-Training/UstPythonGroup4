from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField, RadioField, TextField, TextAreaField 
from wtforms.validators import DataRequired, EqualTo, ValidationError , NumberRange


class AddCourseForm(FlaskForm):
    coursename=StringField("Course Name : ",validators=[DataRequired()])
    courseduration=IntegerField("Course Duration:",validators=[DataRequired(),NumberRange(min=1)])
    coursefee=IntegerField("Course Fee:",validators=[DataRequired(),NumberRange(min=1000)])
    coursestatus=RadioField("Course Status:",choices = [('Active','Active'),('Inactive','Inactive')])
    coursediscription=TextAreaField("Course Discription:",validators=[DataRequired()])
    submit=SubmitField("Add Course")

class ModifyCourseForm(FlaskForm):
    coursename=StringField("Course Name : ",)
    courseduration=IntegerField("Course Duration:",validators=[NumberRange(min=1)])
    coursefee=IntegerField("Course Fee:",validators=[NumberRange(min=1000)])
    coursestatus=RadioField("Course Status:",choices = [('Active','Active'),('Inactive','Inactive')])
    coursediscription=TextAreaField("Course Discription:")
    submit=SubmitField("Edit Course")