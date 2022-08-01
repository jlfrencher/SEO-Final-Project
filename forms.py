from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Email, EqualTo

class RegistrationForm(FlaskForm):  
    name = StringField('',
                       validators=[DataRequired()])

    group_id = IntegerField('',
                           validators=[DataRequired(), NumberRange(min=10000000, max=99999999)])

    email = StringField('',
                        validators=[DataRequired(), Email()])

    password = PasswordField('', validators=[DataRequired()])

    confirm_password = PasswordField('',
                                     validators=[DataRequired(), EqualTo('password')])
                              
    submit = SubmitField('Sign Up') 


class LoginForm(FlaskForm):
    email = StringField('',
                        validators=[DataRequired()])

    password = PasswordField('', validators=[DataRequired()])

    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Log In')