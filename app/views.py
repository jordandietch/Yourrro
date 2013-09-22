from flask import render_template, flash, redirect
from app import app
from forms import Submit
from emailForm import emailForm
import smtplib

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = Submit()
    if form.validate_on_submit():
        emailForm(form)
        return render_template('index.html',
		title = 'RRO: Rapid Real Estate Offer')
    return render_template('submit.html', 
        title = 'RRO: Rapid Real Estate Offer',
        form = form)