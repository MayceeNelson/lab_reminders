from random import choice, randint
from datetime import datetime
import crud
import model

from server import app

model.connect_to_db(app)
model.db.create_all()


for n in range(5):
    email = f'user{n}@test.com'
    password = 'test'
    user1 = crud.create_user(email, password)
    for s in range(10):
        message = "This is Canon Professional Wellness Clinic reminding you of your blood work that needs completed tomorrow as discussed at your last visit with your primary care provider. "
        date_to_send = "10/23/2001"
        date_to_remind="10/24/2001"
        
        # patient = crud.new_patient("12345","bob")

        # schedule = crud.new_schedule(message,
        #                              date_to_send,
        #                              date_to_remind,
        #                              user1,
        #                              patient,
        #                              )
        # schedule.user = user1
        # model.db.session.add(patient)


   
    model.db.session.add(user1)

model.db.session.commit()
