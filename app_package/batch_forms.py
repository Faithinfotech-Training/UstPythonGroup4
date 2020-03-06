from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, RadioField, SubmitField
from wtforms.validators import DataRequired

class AddBatchForm(FlaskForm):  		
	batch_name=StringField("Batch Name: ",validators=[DataRequired()])
	start_date=DateTimeField("Start date: ", validators=[DataRequired()])	
	end_date=DateTimeField("End date: ", validators=[DataRequired()])
	course_id=IntegerField("Course ID: ", validators=[DataRequired()])   
	b_status=RadioField('Status: ', choices = [('Active','Active'),('Inactive','Inactive')])
	submit=SubmitField("Submit")

class ModifyBatchForm(FlaskForm):
   
    start_date=DateTimeField("Start Date: ")
    end_date=DateTimeField("End Date: ")
    b_status=RadioField('Status: ', choices = [('Active','Active'),('Inactive','Inactive')])
    submit=SubmitField("Update")
    