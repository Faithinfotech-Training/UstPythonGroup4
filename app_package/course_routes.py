from flask import render_template,redirect,url_for,flash
from app_package import app,mongo
from flask_login import current_user,login_user,logout_user,login_required
from app_package.course_forms import AddCourseForm, ModifyCourseForm

course_id=0
check=True

@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/display_course")
def display_course():
    course_col=mongo.db.courses
    courses=course_col.find()
    return render_template("display_course.html",courses=courses)

@app.route("/add_course",methods=["GET","POST"])
def add_course():
    global course_id,check
    form=AddCourseForm()
    if form.validate_on_submit():
        fields=["_id","coursename","courseduration","coursefee","coursestatus","coursediscription"]
        course_col=mongo.db.courses
        if check:
                check=False
                if course_col.count()==0:
                    course_id=0
                else:
                    course=course_col.find().sort("_id",-1).limit(1)
                    tmp=course.next()
                    course_id=tmp["_id"] 
        course_id+=1
        values=[course_id,form.coursename.data,form.courseduration.data,form.coursefee.data,form.coursestatus.data,form.coursediscription.data]
        course=dict(zip(fields,values))
        query_name={"coursename":form.coursename.data}
        
        name_check=course_col.find_one(query_name)
        if not bool(name_check) :
            tmp=course_col.insert_one(course)
            if tmp.inserted_id==course_id:
                flash("Course added")
                return redirect(url_for("display_course"))
        else:
            flash("Course Already added")
            return redirect(url_for("add_course"))
    else:
        return render_template("add_course.html",form=form)

@app.route("/modify_course/<int:a>",methods=["GET","POST"])
def modify_course(a):
    form=ModifyCourseForm()
    course_col=mongo.db.courses
    course=course_col.find_one({"_id":a})
    if form.validate_on_submit():
        values=dict()
       
        if form.courseduration.data!="":values["courseduration"]=form.courseduration.data
        if form.coursefee.data!="":values["coursefee"]=form.coursefee.data
        if form.coursestatus.data!="":values["coursestatus"]=form.coursestatus.data
        if form.coursediscription.data!="":values["coursediscription"]=form.coursediscription.data
        new_data={"$set":values}
        query={"_id":a}
        course_col=mongo.db.courses
        course_col.update_one(query,new_data)      
        flash("Course modified")
        return redirect(url_for("display_course"))
    else:
        return render_template("modify_course.html",form=form,course=course)  
@app.route("/back")
def back():
    return redirect(url_for("display_course"))