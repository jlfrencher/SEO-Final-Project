from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
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
    return render_template('home.html', name=current_user.name)


@main.route("/home/update", methods=['GET','POST'])
@login_required
def updateData():
    if request.method == 'GET':
        data = {
            'company': get_company_calendar(current_user.group_id),
            'personal': get_user_calendar(current_user.id)
        }
        return jsonify(data)

    if request.method == 'POST':
        data = request.json

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
        return 'Success', 200

@main.route("/home/id", methods=['GET'])
@login_required
def getID():
    return jsonify({'id': getLastID(current_user.id), 'name': current_user.name})