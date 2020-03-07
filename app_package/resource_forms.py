from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField,RadioField
from wtforms.validators import DataRequired, EqualTo,NumberRange


class AddResourceForm(FlaskForm):
    res_name=StringField("Resource name: ",validators=[DataRequired()])
    res_capacity=IntegerField("Capacity: ",validators=[DataRequired(),NumberRange(min=10)])
    res_status=RadioField("Resource status: ",choices=[('available','available'),('inavailable','inavailable')])
    res_rent=IntegerField("Resource rent: ",validators=[DataRequired(),NumberRange(min=1000)])
    type_of_use=StringField("Type of user: ",validators=[DataRequired()])
    submit=SubmitField("Create new resource")
    
class UpdateResourceForm(FlaskForm):
   
    res_capacity=IntegerField("new capacity: ",validators=[NumberRange(min=10)])
    res_status=RadioField("Resource status: ",choices=[('available','available'),('inavailable','inavailable')])
    res_rent=IntegerField("Enter the rent : ",validators=[NumberRange(min=1000)])
    type_of_use=StringField("Type of use : ")
    submit=SubmitField("update")