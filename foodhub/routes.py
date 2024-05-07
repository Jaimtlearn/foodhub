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
            'username': form.username.data,
            'email': form.email.data,
            'password': hased_pass
        }
        db.insert_one(user)
        flash(f'Account created : {form.username.data}!','success')
        return redirect(url_for('LogIn'))
    return render_template('signup.html',form=form)

@app.route('/login',methods=['GET','POST'])
def LogIn():
    form = LogInForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        results = db.find({"$and": [{"username":form.username.data},{"email":form.email.data}]})
        for data in results:
            print(data)
        return redirect(url_for('Home'))
    return render_template('login.html',form=form)
