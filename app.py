from flask import Flask, render_template
from forms import 
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/signup')
def SignUp():
    return render_template('signup.html',)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")