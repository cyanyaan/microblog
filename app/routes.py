from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Ankit'}
    posts = [
        {
            'author': {'username': 'hateniggers'},
            'body': 'kys nigger'
        },
        {
            'author': {'username': 'jewdestroyer1000'},
            'body': 'i hope the muslims and juice kill eachother'
        }
    ]
    return render_template('index.html', title= 'Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title = "Sign in", form = form)
