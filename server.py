from flask import Flask,render_template,request,flash,session,redirect
from model import connect_to_db, db
import crud
from datetime import datetime
from jinja2 import StrictUndefined
import smtplib, ssl

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route("/")
def home_page():
    """View home page"""
    
    return render_template("homepage.html")



@app.route("/login", methods =["GET","POST"])
def process_login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = crud.get_user_by_email(email)
        
        if not user or user.password != password:
            flash("email or password incorrect.")
        else:
            flash("Login complete!")
            session['email'] = email
            
        return redirect("/")
    elif request.method =="GET":
        return render_template("login_page.html")



@app.route("/users", methods=["POST"])
def register_user():
    """Create a new users."""

    email = request.form.get("email")
    password = request.form.get("password")
    
    if crud.get_user_by_email(email):

        flash("Can't use that email to create account! Try again")
        
    else:    

        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        
    return redirect("/login")




@app.route("/patients", methods=["GET", "POST"])
def register_patient():
    """Create a new patient."""
    if request.method == 'GET':

        patients = crud.get_patients()
        schedules = crud.get_schedules()
        return render_template("all_patients.html", patients = patients,schedules=schedules)

    elif request.method == 'POST':
        phone_num = request.form.get("phone_num")
        name = request.form.get("name")
        print(name)
        schedule= request.form.get("schedule")   
        date_to_send = request.form.get("date_to_send")
        date_to_remind = request.form.get("date_to_remind")
        email =session["email"]
        patient_email=request.form.get("email")
        user = crud.get_user_by_email(email)

        created_patient = crud.new_patient(phone_num,name,schedule,patient_email)
        patient_schedule = crud.new_schedule("This is Canon Professional Wellness Clinic reminding you of your blood work that needs completed tomorrow as discussed at your last visit with your primary care provider. ",date_to_send, date_to_remind, user,created_patient)
        db.session.add(created_patient)
        db.session.add(patient_schedule)
        db.session.commit()
        
        
        return redirect("/patients")

@app.route("/schedule/<schedule_id>", methods =['POST'])
def new_schedule(schedule_id):
    message =crud.get_patient_by_name(message)
    date_to_send= crud.get_date_to_send(date_to_send)
    date_to_remind= crud.get_date_to_remind(date_to_remind)
    schedule = crud.create_schedule(message, date_to_send, date_to_remind)
    db.session.add(schedule)
    db.session.commit()
    return redirect("/")


@app.route("/send-message",methods=["POST"])
def send_message():
    schedule_id=request.json.get("schedule_id")
    schedule = crud.get_schedule_by_id(schedule_id)
    send_email(schedule)
    return{
        "status":"Message sent!"
    }

def send_email(schedule):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "maggiedatlon@gmail.com"  # Enter your address
    receiver_email = schedule.patient.email  # Enter receiver address
    receiver_txt_sms =schedule.patient.email
    password = "asvj kofy ulct qodi"
    message = schedule.message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_txt_sms, message)

@app.route("/check-message")
def check_message():
    all_schedules = crud.get_schedules()
    today = datetime.today().date()
    for schedule in all_schedules:
        if schedule.date_to_send.date() == today:
            send_email(schedule)
            print(schedule)
    return ""





if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)