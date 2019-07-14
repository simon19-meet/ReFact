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

@app.route('/signup', methods=['GET','POST'])
def signup():
	if request.method == 'POST':
		if request.form['choice'] == "volunteer":
			return redirect(url_for('volunteer_signup'))
		elif request.form['choice'] == "refugee":
			return redirect(url_for('refugee_signup'))
		else:
			return redirect(url_for('Login'))
	return render_template("signup.html")

@app.route('/stories',methods=['GET'])
def stories():
	if request.method=='GET':
		stories=query_all_stories()
		return render_template('stories.html', stories=stories)

@app.route('/share',methods=['GET','POST'])
def share():
	if request.method=='POST':
		if login_session['type'] == 'refugee':
			refugee=query_refugee_by_email(login_session['email'])
			add_story(refugee.name, refugee.email,refugee.age, request.form['content'])
			return redirect(url_for('stories'))
		else:
			return redirect(url_for('home'))
	if request.method=='GET':
		stories=query_all_stories()
		return render_template('share.html',stories=stories)

@app.route('/activities',methods=['GET','POST'])
def Activities():
	if request.method=='GET':
		activities=query_all_activities()
		return render_template('activities.html', activities=activities)

@app.route('/activity/<int:activity_id>',methods=['GET','POST'])
def Activity(activity_id):
	if request.method=='POST':
		if login_session['type']=='refugee':
			activity=query_activity_by_id(activity_id)
			update_activity_refugee(activity_id,activity.refugees+1)
		if login_session['type']=='volunteer':
			activity=query_activity_by_id(activity_id)
			name=login_session['name']
			update_activity_volunteer(activity_id,activity.volunteers+name)
	if request.method=='GET':
		activity=query_activity_by_id(activity_id)
		return render_template('activities.html', activity=activity)

@app.route('/add_activity',methods=['GET','POST'])
def Add_activity():
	if request.method=='POST':
		volunteer=query_volunteer_by_email(login_session['email'])
		add_activity(request.form['name'], request.form['description'], request.form['age'], 
			request.form['date'], request.form['location'], volunteer.name)
		return redirect(url_for('home'))
	if request.method=='GET':
		return render_template('add_activity.html')

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
			login_session['type'] = 'volunteer'
			return redirect(url_for('home'))
		return redirect(url_for('Login'))
	if request.method=='GET':
		return render_template('login.html')

@app.route('/refugee_signup',methods=['GET','POST'])
def refugee_signup():
	if request.method=='POST':
		signup_refugee(request.form['name'],
			request.form['email'],
			request.form['password'],
			request.form['gender'],
			request.form['age'])
		return redirect(url_for('home'))
	if request.method=='GET':
		return render_template('refugee_signup.html')

@app.route('/volunteer_signup',methods=['GET','POST'])
def volunteer_signup():
	if request.method=='POST':
		signup_volunteer(request.form['name'],
			request.form['email'],
			request.form['password'],
			request.form['gender'],
			request.form['age'])
		return redirect('/')
	if request.method=='GET':
		return render_template('volunteer_signup.html')

@app.route('/contact_us',methods=['GET'])
def contact_us():
	if request.method=='GET':
		return render_template('contact.html')

@app.route('/logout')
def logout():
	login_session.clear()
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)

