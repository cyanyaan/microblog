from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/sex')
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