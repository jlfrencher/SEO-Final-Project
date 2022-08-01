from models import *
from extensions import db
from datetime import time

def get_company_calendar(group_id):
    all_items = Slot.query.filter_by(group_id=group_id).all()

    return { 'data': [item.to_dict() for item in all_items] }


def get_user_calendar(user_id):
    all_items = Slot.query.filter_by(user_id=user_id).all()

    return { 'data': [item.to_dict() for item in all_items] }


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
    query = Slot.query.filter_by(id=id).first()
    
    if query:
        data = query.to_dict()
        query.delete()
        db.session.commit()
        return data
    else:
        return None


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
    
