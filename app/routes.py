from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ilya'}
    posts = [
        {
            'author': {'username': 'Marquez'},
            'body': 'Beautiful day in Spain!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Master Yoda'},
            'body': 'English learn you must!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
    
