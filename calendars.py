from models import *
from extensions import db
from datetime import datetime, time, timedelta

def get_company_calendar(group_id):
    all_items = Slot.query.filter_by(group_id=group_id).all()

    return [
        {**item.to_dict(),
        **{
            'name': User.query.filter_by(id=item.user_id).first().name
        }} 
        for item in all_items
    ]


def get_user_calendar(user_id):
    all_items = Slot.query.filter_by(user_id=user_id).all()

    return [item.to_dict() for item in all_items]


def add_slot(group_id, user_id, date, start_time=time(0), end_time=time(0)):
    new_slot = Slot(
        group_id = group_id,
        user_id = user_id,
        date = date,
        start_time = start_time,
        end_time = end_time
    )
    db.session.add(new_slot)
    db.session.commit()


def remove_slot(id):
    query = Slot.query.filter_by(id=id)
    
    if query:
        query.delete()
        db.session.commit()


def update_slot(id, date=None, start_time=None, end_time=None):
    selected_slot = Slot.query.filter_by(id=id)

    if not selected_slot:
        return
    
    if date:
        selected_slot.update({'date': date})

    if start_time:
        selected_slot.update({'start_time': start_time})
    
    if end_time:
        selected_slot.update({'end_time': end_time})
    
    db.session.commit()
    
def getLastID(user_id):
    query = Slot.query.order_by(Slot.id.desc()).first()
    return query.id

def createMeeting(start_date, end_date):
    if start_date > end_date:
        return
    
    numDays = (end_date - start_date).days()
    data = []

    for i in range(numDays):
        query = Slot.query.filter_by(date=(start_date + timedelta(days=i)))
        data[i].push(query.count())

    max_index = data.index(max(data))

    all_users = Slot.query.filter_by(date=(start_date + max_index)).all()
    pass
