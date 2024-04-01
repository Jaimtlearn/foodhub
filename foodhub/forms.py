from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignUpForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(),Length(min=8,max=20)],render_kw={"placeholder": "Username"})
    email = EmailField('Email',validators=[DataRequired(),Email()],render_kw={"placeholder": "random@gmail.com"})
    password = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=60)],render_kw={"placeholder": "**********"})
    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(),Length(min=6,max=60),EqualTo('password')],render_kw={"placeholder": "**********"})
    submit = SubmitField('SignUp')

class LogInForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(),Email()])
    pasword = PasswordField('Password',validators=[DataRequired(),Length(min=6,max=60)])
    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(),Length(min=6,max=60),EqualTo('password')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('LogIn')