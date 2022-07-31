from flask import Blueprint, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm
from flask_login import login_required, current_user
from calendars import *

main = Blueprint('main', __name__)

product_name = "Hybrid Schedule"

@main.route("/")
def info():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
        return render_template('info.html', title=f'{product_name}')

@main.route("/home", methods=['POST'])
@login_required
def home():
    company_data = get_company_calendar(current_user.group_id)
    personal_data = get_user_calendar(current_user.id)

    return render_template(
        'home.html',
        title=f'{product_name}',
        name=current_user.name,
        company_data=company_data,
        personal_data=personal_data
    )