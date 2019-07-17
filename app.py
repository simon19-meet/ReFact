from flask import Flask, render_template, url_for, redirect, request
from database import *
from flask import session as login_session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/',methods=['GET','POST'])
def home():
	if request.method=='POST':
		add_feedback(request.form['name'],request.form['age'],request.form['content'])
		return redirect(url_for('home'))
	if request.method=='GET':
		return render_template('home.html')

@app.route('/about_us',methods=['GET'])
def about_us():
	if request.method=='GET':
		return render_template('about_us.html')

@app.route('/volunteer_signup', methods=['GET', 'POST'])
def volunteering():
	if request.method=='POST':
		volunteer(request.form['name'], 
			request.form['email'], 
			request.form['gender'], 
			request.form['age'], 
			request.form['number'], 
			request.form['address'], 
			request.form['work'], 
			request.form['academic_level'])
		return redirect(url_for('thank_you'))
	if request.method=='GET':
		return render_template('volunteer.html')

@app.route('/donations', methods=['GET', 'POST'])
def donations():
	if request.method=='GET':
		return render_template('donations.html')

@app.route('/thank_you', methods=['GET'])
def thank_you():
	if request.method=='GET':
		return render_template('thank_you.html')

@app.route('/contact', methods=['GET'])
def contact():
	if request.method=='GET':
		return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)

