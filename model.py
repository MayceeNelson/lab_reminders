from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    schedule = db.relationship("Schedule", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Schedule(db.Model):
    """scheduling a message."""

    __tablename__ = "schedule"

    schedule_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    message= db.Column(db.String)
    date_to_send= db.Column(db.DateTime)
    date_to_remind= db.Column(db.DateTime)
    patient_id= db.Column(db.Integer,db.ForeignKey("patients.patient_id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.user_id"))
    
    # back_populates is the name of the relationship in the other class
    patient = db.relationship("Patients", back_populates="schedule")
    
    user = db.relationship("User", back_populates="schedule")

    def __repr__(self):
        return f'<Schedule schedule_id={self.schedule_id} date to send ={self.date_to_send}>'
        
class Patients(db.Model):
    """saving a patient."""

    __tablename__ = "patients"

    patient_id= db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email= db.Column(db.String)
    phone_num= db.Column(db.String)
    name= db.Column(db.String)
    schedule =db.relationship("Schedule", back_populates="patient")
    def __repr__(self):
        return f'<patient patient_id={self.patient_id} name={self.name}>'


def connect_to_db(flask_app, db_uri="postgresql:///reminders", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)


# user1 = User(email='', password='')
# schedule = Schedule(...)
# schedule.user = users1