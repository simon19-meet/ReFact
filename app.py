from flask import Flask, render_template, url_for, redirect, request
from database import *
from flask import session as login_session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/',methods=['GET'])
def home():
	if request.method=='GET':
		return render_template('home.html')

@app.route('/stories',methods=['GET'])
def stories():
	if request.method=='GET':
		return render_template('stories.html')

@app.route('/share',methods=['GET','POST'])
def share():
	if request.method=='POST':
		refugee=query_user_by_email(login_session['email'])
		add_story(refugee.name, refugee.email, refugee.age, request.form['content'])
		return redirect(url_for('stories'))
	if request.method=='GET':
		stories=query_all_stories()
		return render_template('share.html')

@app.route('/activities',methods=['GET','POST'])
def Activities():
	if request.method=='POST':
		
	if request.method=='GET':
		activities=query_all_activities()
		return render_template('activities.html')

@app.route('/donate',methods=['GET','POST'])
def Donate():
	if request.method=='GET':
		return render_template('donate.html')

@app.route('/login',methods=['GET','POST'])
def Login():
	if request.method=='POST':
		refugee=query_refugee_by_email(request.form['email'])
		volunteer=query_volunteer_by_email(request.form['email'])
		if refugee!=None and refugee.password==request.form['password']:
			login_session['name'] = refugee.name
			login_session['email'] = refugee.email
			login_session['type'] = 'refugee'
			return redirect(url_for('home'))
		if volunteer!=None and volunteer.password==request.form['password']:
			login_session['name'] = volunteer.name
			login_session['email'] = volunteer.email
			login_session['type'] = 'vounteer'
			return redirect(url_for('home'))
		return redirect(url_for('Login'))
	if request.method=='GET':
		return render_template('login.html')

@app.route('/signup_refugee',methods=['GET','POST'])
def signup_refugee():
	if request.method=='POST':
		signup_refugee(request.form['name'],
			request.form['email'],
			request.form['password'],
			request.form['gender'],
			request.form['age'],)
	if request.method=='GET':
		return render_template('refugee_signup.html')

@app.route('/signup_volunteer',methods=['GET','POST'])
def signup_volunteer():
	if request.method=='POST':
		signup_volunteer(request.form['name'],
			request.form['email'],
			request.form['password'],
			request.form['gender'],
			request.form['age'],)
	if request.method=='GET':
		return render_template('volunteer_signup.html')

@app.route('/contact_us',methods=['GET'])
def contact_us():
	if request.method=='GET':
		return render_template('contact.html')

@app.route('/logout')
def logout():
	del login_session['email']
	del login_session['name']
	del login_session['type']
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)

