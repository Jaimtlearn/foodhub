from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignUpForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(),Length(min=8,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=60)])
    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(),Length(min=6,max=60),EqualTo('password')])
    submit = SubmitField('SignUp')

class LogInForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    pasword = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=60)])
    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(),Length(min=6,max=60),EqualTo('password')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('LogIn')