import json
import os
from datetime import datetime, time
from werkzeug.security import generate_password_hash, check_password_hash

# Formula for times in mockaroo
# (this - (this.min() - ((this.min()+8)/15)*900)).strftime('%H:%M')

def createFakeSlots(app, db, Slot):
    with app.app_context():
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        try:
            file = open(os.path.join(__location__, 'MOCK_SLOTS.json'))
            data = json.load(file)

            for item in data:
                new_slot = Slot(
                    group_id = item['group_id'],
                    user_id = item['user_id'],
                    date = datetime.strptime(item['date'], "%Y/%m/%d"),
                    start_time = datetime.strptime(item['start_time'], '%H:%M').time(),
                    end_time = datetime.strptime(item['end_time'], '%H:%M').time()
                )
                db.session.add(new_slot)
            db.session.commit()
        except FileNotFoundError as e:
            print("File not found")


def createFakeUsers(app, db, User):
    with app.app_context():
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        try:
            file = open(os.path.join(__location__, 'MOCK_USERS.json'))
            data = json.load(file)

            for item in data:
                new_slot = User(
                    name = item['name'],
                    group_id = item['group_id'],
                    email = item['email'],
                    password = generate_password_hash(item['password'], method='sha256')
                )
                db.session.add(new_slot)
            db.session.commit()
        except FileNotFoundError as e:
            print("File not found")