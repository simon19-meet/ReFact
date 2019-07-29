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

@app.route('/material_he', methods=['GET'])
def material_he():
	if request.method=='GET':
		return render_template('material_he.html')

@app.route('/material_ar', methods=['GET'])
def material_ar():
	if request.method=='GET':
		return render_template('material_ar.html')

@app.route('/paypal', methods=['GET'])
def paypal():
	if request.method=='GET':
		return render_template('paypal.html')

@app.route('/paypal_he', methods=['GET'])
def paypal_he():
	if request.method=='GET':
		return render_template('paypal_he.html')

@app.route('/paypal_ar', methods=['GET'])
def paypal_ar():
	if request.method=='GET':
		return render_template('paypal_ar.html')

@app.route('/',methods=['GET','POST'])
def home():
	if request.method=='GET':
		return render_template('home.html')

@app.route('/he',methods=['GET','POST'])
def home_he():
	if request.method=='GET':
		return render_template('home_he.html')

@app.route('/ar',methods=['GET','POST'])
def home_ar():
	if request.method=='GET':
		return render_template('home_ar.html')

@app.route('/about_us',methods=['GET'])
def about_us():
	if request.method=='GET':
		return render_template('about_us.html')

@app.route('/about_us_he',methods=['GET'])
def about_us_he():
	if request.method=='GET':
		return render_template('about_us_he.html')
		
@app.route('/about_us_ar',methods=['GET'])
def about_us_ar():
	if request.method=='GET':
		return render_template('about_us_ar.html')

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

@app.route('/volunteer_signup_he', methods=['GET', 'POST'])
def volunteering_he():
	if request.method=='POST':
		volunteer(request.form['name'], 
			request.form['email'], 
			request.form['gender'], 
			request.form['age'], 
			request.form['number'], 
			request.form['address'], 
			request.form['work'], 
			request.form['academic_level'])
		return redirect(url_for('thank_you_he'))
	if request.method=='GET':
		return render_template('volunteer_he.html')

@app.route('/volunteer_signup_ar', methods=['GET', 'POST'])
def volunteering_ar():
	if request.method=='POST':
		volunteer(request.form['name'], 
			request.form['email'], 
			request.form['gender'], 
			request.form['age'], 
			request.form['number'], 
			request.form['address'], 
			request.form['work'], 
			request.form['academic_level'])
		return redirect(url_for('thank_you_ar'))
	if request.method=='GET':
		return render_template('volunteer_ar.html')

@app.route('/donations', methods=['GET', 'POST'])
def donations():
	if request.method=='GET':
		return render_template('donations.html')

@app.route('/donations_he', methods=['GET', 'POST'])
def donations_he():
	if request.method=='GET':
		return render_template('donations_he.html')
		
@app.route('/donations_ar', methods=['GET', 'POST'])
def donations_ar():
	if request.method=='GET':
		return render_template('donations_ar.html')

@app.route('/thank_you', methods=['GET'])
def thank_you():
	if request.method=='GET':
		return render_template('thank_you.html')

@app.route('/thank_you_he', methods=['GET'])
def thank_you_he():
	if request.method=='GET':
		return render_template('thank_you_he.html')
		
@app.route('/thank_you_ar', methods=['GET'])
def thank_you_ar():
	if request.method=='GET':
		return render_template('thank_you_ar.html')

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

@app.route('/share_he', methods=['GET','POST'])
def share_he():
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
		return redirect(url_for('view_he',c=c))
	return render_template('share_he.html')

@app.route('/share_ar', methods=['GET','POST'])
def share_ar():
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
		return redirect(url_for('view_ar',c=c))
	return render_template('share_ar.html')

@app.route('/view_stories',methods=['GET'])
def view():
	print("hello viewer")
	if request.method=='GET':
		stories=display_stories()
		return render_template('view_stories.html',stories=stories)

@app.route('/view_stories_he',methods=['GET'])
def view_he():
	print("hello viewer")
	if request.method=='GET':
		stories=display_stories()
		return render_template('view_stories_he.html',stories=stories)

@app.route('/view_stories_ar',methods=['GET'])
def view_ar():
	print("hello viewer")
	if request.method=='GET':
		stories=display_stories()
		return render_template('view_stories_ar.html',stories=stories)

@app.route('/insert',methods=['POST','GET'])
def insert():
	if request.method=='POST':
		number=request.form['number']
		place=request.form['place']
		date=request.form['date']
		numppl=request.form['numppl']
		aim=request.form['aim']
		info=request.form['info']
		add_program(number,place,date,numppl,aim,info)
		return redirect(url_for('show'))
	return render_template('insert.html')

@app.route('/info',methods=['GET','POST'])
def show():
	if request.method == 'GET':
		programs=display_programs()
		return render_template('info.html',programs=programs)

if __name__ == '__main__':
	app.run(debug=True)

