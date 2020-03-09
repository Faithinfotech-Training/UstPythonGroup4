from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired



class AddQualificationForm(FlaskForm):
	qualname=SelectField("Qualification Name:", validators=[DataRequired()])
	coursename=StringField("Course Name:" ,validators=[DataRequired()])
	submit=SubmitField("submit")

class QualificationForm(FlaskForm):
	coursename=SelectField("Course :",validators=[DataRequired()])	
	submit=SubmitField("Add ")


class DisplayQualificationForm(FlaskForm): 
	qualiid=IntegerField("Qualification Id:",validators=[DataRequired()])
	qualiname=StringField("Qualification Name:", validators=[DataRequired()])


