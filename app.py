from flask import Flask, render_template
from forms import SignUpForm, LogInForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2ef5ceadc6fac9ebf18423903ba4816'

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/signup')
def SignUp():
    form = SignUpForm()
    return render_template('signup.html',form=form)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")