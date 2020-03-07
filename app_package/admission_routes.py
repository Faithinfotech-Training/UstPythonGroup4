from flask import render_template,flash,redirect,url_for
from app_package import app,mongo
from flask_login import current_user,login_user,logout_user,login_required
from app_package.admission_forms import AdmissionSearchForm,AdmissionAddForm

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
    form=AdmissionAddForm()
    global a_id
    global check

    if form.validate_on_submit():
        fields=["_id","ad_name","ad_gender","ad_phone","ad_email","ad_qualification","ad_year_of_pass","batch_name","ad_guardianname","ad_guardianphone","ad_address"]
        ad_col=mongo.db.admission
        if check:
            check=False
            if ad_col.count()==0: 
                a_id=0
            else:
                ad=ad_col.find().sort("_id",-1).limit(1)
                tmp=ad.next()
                a_id=tmp["_id"]
        a_id+=1
        
        values=[a_id,form.e_name.data,form.e_gender.data,form.e_phone.data,form.e_email.data,form.e_qualification.data,form.e_year_of_pass.data,form.batch_name.data,form.e_guardianname.data,form.e_guardianphone.data,form.e_address.data]
        candidate=dict(zip(fields,values))
        tmp=ad_col.insert_one( candidate)
        if tmp.inserted_id==a_id:
            flash(" Candidate Added")
            return redirect(url_for("Admissionhome"))
        else:
            flash("Problem in adding Candidate")
            return redirect(url_for("Admissionhome")) 
    else:
        flash(" Cannot submit")
        return redirect(url_for("Admissionhome"))

    

@app.route("/displayAdmitted",methods=["GET"])
def admission_data():
    ad_col=mongo.db.admission
    admits=ad_col.find()
    return render_template("display_admission.html",admits=admits)