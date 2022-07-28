from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])

    groupID = IntegerField('Group ID',
                           validators=[DataRequired(), Length(min=8, max=8)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
                                     
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Username',
                        validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Log In')