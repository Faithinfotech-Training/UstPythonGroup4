from flask import render_template,flash,redirect,url_for
from app_package import app,mongo
from flask_login import current_user,login_user,logout_user,login_required
from app_package.forms import EnquiryForm,UpdateDataForm,EnquirySearchForm

check=True
cust_id=0


@app.route("/enquiryForm", methods=["GET","POST"])
def enquiry():
    global cust_id
    global check
    form=EnquiryForm()
    if form.validate_on_submit():
        fields=["_id","name","phone_number","email","passout_year","course","qualification","place","status"]
        cust_col=mongo.db.customers
        if check:
            check=False
            if cust_col.count()==0: 
                cust_id=0
            else:
                cust=cust_col.find().sort("_id",-1).limit(1)
                tmp=cust.next()
                cust_id=tmp["_id"]
        cust_id+=1
        values=[cust_id,form.name.data,form.phone_number.data,form.email.data,form.passout_year.data,form.course.data,form.qualification.data,form.place.data,form.status.data]
        customer=dict(zip(fields,values))
        cust_col=mongo.db.customers
        tmp=cust_col.insert_one(customer)
        if tmp.inserted_id==cust_id:
            flash("Enquiry Submitted")
            return redirect(url_for("enquiry_data"))
        else:
            flash("Problem adding Details")
            return redirect(url_for("enquiry"))
    else:
        return render_template("enquiry_form.html",form=form) 
    return render_template("enquiry_fail.html",form=form)

@app.route("/display",methods=["GET"])
def enquiry_data():
    cust_col=mongo.db.customers
    customers=cust_col.find()
    return render_template("display_enquiries.html",customers=customers)
    
@app.route("/modifyData/<int:enquiry_id>",methods=["GET","POST"])
def update_customer(enquiry_id):
    form=UpdateDataForm()
    enq_col=mongo.db.customers
    enquiry=enq_col.find_one({"_id":enquiry_id})
    if form.validate_on_submit():
        values=dict()
        values["phone_number"]=form.phone_number.data
        values["email"]=form.email.data
        values["status"]=form.status.data
        values["name"]=form.name.data
        values["passout_year"]=form.passout_year.data
        values["place"]=form.place.data
        values["qualification"]=form.qualification.data
        values["course"]=form.course.data
        new_data={"$set":values}
        query={"_id":enquiry_id}
        cust_col=mongo.db.customers
        cust_col.update_one(query,new_data)
        flash("Modified the Customer Details")
        return redirect(url_for('enquiry_data'))
    else:
        return render_template("update_enquiry.html",form=form,enquiry=enquiry)


@app.route("/enquirysearch",methods=["GET","POST"])
def enquirysearch():
    form=EnquirySearchForm()
    if form.validate_on_submit:
        e_col=mongo.db.customers
        search=form.e_type.data
        if search=='Enquiry Id':
            e_id=int(form.e_name.data)
            e_query={"_id":e_id}
            e_data=e_col.find(e_query)
            return render_template("searchEnquiryView.html",e_data=e_data)
        elif search=='Name':
            n_query={"name":form.e_name.data}
            e_data=e_col.find(n_query)
            return render_template("searchEnquiryView.html",e_data=e_data)
        elif search=='Phone':
            e_phone=int(form.e_name.data)
            p_query={"phone_number":e_phone}
            e_data=e_col.find(p_query)
            return render_template("searchEnquiryView.html",e_data=e_data)
        elif search=='Status':
            #status=dict(form.status.choices).get(form.status.data)
            e_status=form.e_name.data
            s_query={"status":e_status}
            e_data=e_col.find(s_query)
            return render_template("searchEnquiryView.html",e_data=e_data)
        else:
            return render_template("enquirySearchOption.html",form=form)
    else:
        flash("Not Avilable")
        return render_template("enquirySearchOption.html",form=form)


