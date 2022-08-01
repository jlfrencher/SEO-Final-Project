from flask import Blueprint, render_template, redirect, url_for, flash
from forms import LoginForm, RegistrationForm
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from extensions import db

auth = Blueprint('auth', __name__)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user or not check_password_hash(user.password, form.password.data):
            flash('Please check your login details and try again.', "error")
            return redirect(url_for('auth.signin'))

        print("/n/n", form.remember.data, "/n/n")
        
        login_user(user, remember=form.remember.data)
                
        return redirect(url_for('main.home'))
    return render_template('login.html', title="Sign in/up", form=form, form_type=True)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            flash('Email address already exists', 'error')
            return redirect(url_for('auth.signup'))

        new_user = User(
                    name = form.name.data,
                    group_id = form.group_id.data,
                    email = form.email.data,
                    password = generate_password_hash(form.password.data, method='sha256')
                )
        db.session.add(new_user)
        db.session.commit()

        flash("User created sucessfully! Please sign in below", "success")

        return redirect(url_for("auth.signin"))
    return render_template('login.html', title="Sign in/up", form=form, form_type=False)

@auth.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('main.info'))