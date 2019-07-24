from flask import Flask, render_template, url_for, redirect, request
from database import * 	
from flask import session as login_session
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/material', methods=['GET'])
def material():
	if request.method=='GET':
		return render_template('material.html')

@app.route('/paypal', methods=['GET'])
def paypal():
	if request.method=='GET':
		return render_template('paypal.html')

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

@app.route('/share', methods=['GET','POST'])
def share():
	c=len(session.query(Story).all())
	if request.method=='POST':
		print("hi")
		print(request.form['name'])
		print(request.form['age'])
		print(request.form['content'])

		name=request.form['name']
		age=request.form['age']
		content=request.form['content']
		picBefore=request.files['before']
		picAfter=request.files['after']
		c+=1
		strBef="static/images/before"
		strBef+=str(c)
		strAf="static/images/after"
		strAf+=str(c)
		picBefore.save(strBef)
		picAfter.save(strAf)
		story=Story(name=name,age=age,content=content,before=picBefore.read(),after=picAfter.read())
		session.add(story)
		session.commit()
		return redirect(url_for('view',c=c))
	return render_template('share.html')

@app.route('/view_stories',methods=['GET'])
def view():
	print("hello viewer")
	if request.method=='GET':
		stories=display_stories()
		return render_template('view_stories.html',stories=stories)




if __name__ == '__main__':
	app.run(debug=True)

