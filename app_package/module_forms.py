from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField,SelectField,FloatField
from wtforms.validators import DataRequired,EqualTo,ValidationError,NumberRange
from app_package import app,db,mongo

class CourseForm(FlaskForm):
	coursename=SelectField("Course :",validators=[DataRequired()])
	submit=SubmitField("Add ")
	
class AddModuleForm(FlaskForm):
	coursename=StringField("Course :",validators=[DataRequired()])
	name=SelectField("Modules :",validators=[DataRequired()])
	submit=SubmitField("Add ")


