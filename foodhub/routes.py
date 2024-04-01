from foodhub import app,db,bcrypt
from flask import render_template, flash, redirect, url_for
from foodhub.forms import SignUpForm, LogInForm

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/signup',methods=['GET','POST'])
def SignUp():
    form = SignUpForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        hased_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = {
            'username': 'Jaimit Patel',
            'email': 'jaimitpatel@gmail.com',
            'password': 'hashed'
        }
        flash(f'Account created : {form.username.data}!','success')
        return redirect(url_for('Home'))
    return render_template('signup.html',form=form)