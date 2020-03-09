from flask import render_template,flash,redirect,url_for
from app_package import app,mongo
from flask_login import current_user,login_user,logout_user,login_required
from app_package.admission_forms import AdmissionSearchForm,AdmissionAddForm,AdmissionUpdateForm

a_id=0
check=True
@app.route("/Admissionhome",methods=["GET","POST"])
def Admissionhome():
    form=AdmissionSearchForm()
    f2=AdmissionAddForm()
    batch_col=mongo.db.batchs
    batch=batch_col.find()
    lst=[]
    for i in batch:
        lst.append((i["batch_name"],i["batch_name"]))
    f2.batch_name.choices=lst
    if form.validate_on_submit():
        ad_col=mongo.db.customers
        edata=ad_col.find_one({"phone_number":form.e_phone.data})
        if edata["status"]=='Exam Passed':
            return render_template("admissionForm.html",form=form,f2=f2,edata=edata)
       
        else:
            flash("Not Applicable Student")
            return redirect(url_for("Admissionhome"))
    else:
         return render_template("admissionHome.html",form=form)


@app.route("/Admission_add",methods=["GET","POST"])
def Admission_add():
    global a_id
    global check
    form=AdmissionAddForm()
    batch_col=mongo.db.batchs
    batch=batch_col.find()
    lst=[]
    for i in batch:
        lst.append((i["batch_name"],i["batch_name"]))
    form.batch_name.choices=lst
    if form.validate_on_submit():
        print("hai")
        fields=["_id","e_name","e_gender","e_phone","e_email","e_qualification","e_course_of_interest","e_year_of_pass","e_status","batch_name","e_guardianname","e_guardianphone","e_address"]
        ad_col=mongo.db.admission
        if check:
            check=False
            if ad_col.count()==0: 
                a_id=0
            else:
                a=ad_col.find().sort("_id",-1).limit(1)
                tmp=a.next()
                a_id=tmp["_id"]
        a_id+=1
        values=[a_id,form.e_name.data,form.e_gender.data,form.e_phone.data,form.e_email.data,form.e_qualification.data,form.e_course_of_interest.data,form.e_year_of_pass.data,form.e_status.data,form.batch_name.data,form.e_guardianname.data,form.e_guardianphone.data,form.e_address.data]
        admission=dict(zip(fields,values))
        ad_col=mongo.db.admission
        tmp=ad_col.insert_one(admission)
        if tmp.inserted_id==a_id:
            flash("Candidate Added")
            return redirect(url_for("admission_data"))
        else:
            flash("Problem in adding Candidate")
            return redirect(url_for("admission_data"))
            
    else:
        flash(" Cannot submit")
        return redirect(url_for("admission_data"))
        

@app.route("/admission_display",methods=["GET"])
def admission_data():
    ad_col=mongo.db.admission
    admission=ad_col.find()
    return render_template("display_admission.html",admission=admission)

@app.route("/modifyAdmissionData/<int:enquiry_id>",methods=["GET","POST"])
def update_admission(enquiry_id):
    form=AdmissionUpdateForm()
    batch_col=mongo.db.batchs
    batch=batch_col.find()
    lst=[]
    for i in batch:
        lst.append((i["batch_name"],i["batch_name"]))
    form.batch_name.choices=lst
    ad_col=mongo.db.admission
    admission=ad_col.find_one({"_id":enquiry_id})
    if form.validate_on_submit()==True:
        values=dict()
        values["e_course_of_interest"]=form.e_course_of_interest.data
        values["e_gender"]=form.e_gender.data
        values["e_guardianphone"]=form.e_guardianphone.data
        values["e_guardianname"]=form.e_guardianname.data
        values["batch_name"]=form.batch_name.data
        values["e_phone"]=form.e_phone.data
        values["e_email"]=form.e_email.data
        values["e_name"]=form.e_name.data
        values["e_year_of_pass"]=form.e_year_of_pass.data
        values["e_qualification"]=form.e_qualification.data
        new_data={"$set":values}
        query={"_id":enquiry_id}
        ad_col=mongo.db.admission
        ad_col.update_one(query,new_data)
        flash("Modified the Customer Details")
        return redirect(url_for('admission_data'))
    else:
        return render_template("update_admission.html",form=form,admission=admission)

       
