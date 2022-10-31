from flask import render_template

from app import app
from app.forms import LoginForm

@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    title = 'Sign In'
    form = LoginForm()
    return render_template('login.html', title=title, form=form)