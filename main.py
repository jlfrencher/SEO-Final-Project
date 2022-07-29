from flask import Blueprint, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm
from flask_login import login_required, current_user

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
    return render_template('home.html', title=f'{product_name}', name=current_user.name)