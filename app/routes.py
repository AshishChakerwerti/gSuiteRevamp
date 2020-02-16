from . import app
from flask import render_template


@app.route("/")
def home():
    return "please open /index"


@app.route('/index')
def index():
    return render_template('test.html')
