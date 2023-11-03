from model import User,Schedule,Patients, connect_to_db


def create_user(email,password):

    user = User(email=email, password=password)
    return user

def new_patient(phone_num,name,schedule,patient_email):
    patient = Patients(phone_num = phone_num, name=name, email=patient_email)
    return patient
def get_patients():
    return Patients.query.all()

def new_schedule(message, date_to_send,date_to_remind,user,patient):
    schedule =Schedule(message=message,
        date_to_send= date_to_send,
        date_to_remind=date_to_remind,
        user=user,
        patient=patient)
    
    return schedule

def get_users():

    return User.query.all()


def get_user_by_email(email):

    return User.query.filter(User.email == email).first()


def get_user_by_name(name):
    return User.query.filter(User.name == name).first()

def get_schedules():
    return Schedule.query.all()
def get_schedule_by_id(schedule_id):
    return Schedule.query.filter(Schedule.schedule_id==schedule_id).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)