from flask import Blueprint, render_template, url_for, flash, redirect, request
from forms import LoginForm, RegistrationForm
from flask_login import login_required, current_user
from calendars import *
from datetime import datetime, time
import json

main = Blueprint('main', __name__)

product_name = "Hybrid Schedule"

@main.route("/")
def info():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
        return render_template('info.html', title=f'{product_name}')

@main.route("/home")
@login_required
def home():
    company_data = get_company_calendar(current_user.group_id)
    personal_data = get_user_calendar(current_user.id)
    
    return render_template(
        'home.html',
        title=f'{product_name}',
        name=current_user.name,
        company_data=json.dumps(company_data),
        personal_data=json.dumps(personal_data)
    )

@main.route("/home/update", methods=['POST'])
@login_required
def updateData():
    data = request.json
    print(data['action'])

    if data['action'] == "update":
        update_slot(
            id=data['id'],
            start_time=datetime.strptime(data['start_time'], '%H:%M').time(),
            end_time=datetime.strptime(data['end_time'], '%H:%M').time()
        )
    elif data['action'] == 'add':
        add_slot(
            group_id=current_user.group_id,
            user_id=current_user.id,
            date=datetime.strptime(data['date'], "%m/%d/%Y"),
            start_time=datetime.strptime(data['start_time'], '%H:%M').time(),
            end_time=datetime.strptime(data['end_time'], '%H:%M').time()
        )
    elif data['action'] == 'remove':
        remove_slot(data['id'])

    return redirect(url_for('main.home'))