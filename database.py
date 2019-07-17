
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_feedback(name, age, content):
	feedback_object = Feedback(
		name=name,
		age=age,
		content=content)
	session.add(feedback_object)
	session.commit()

def volunteer(name, email, gender, age, number, address, work, academic_level):
	volunteer_object = Volunteer(
		name=name,
		email=email,
		gender=gender,
		age=age,
		number=number,
		address=address,
		work=work,
		academic_level=academic_level)
	session.add(volunteer_object)
	session.commit()



# ///////////////////////////////////////////////////////////////////////////////////////////////////

def add_activity(name, description, age, date, location, leader):
	activity_object = Activity(
		name=name,
		description=description,
		age=age,
		date=date,
		location=location,
		leader=leader)
	session.add(activity_object)
	session.commit()

def query_refugee_by_email(email):
	refugee = session.query(Refugee).filter_by(email=email).first()
	return refugee

def query_volunteer_by_email(email):
	volunteer = session.query(Volunteer).filter_by(email=email).first()
	return volunteer

def query_all_stories():
	stories = session.query(Story).all()
	return stories

def query_all_activities():
	activities = session.query(Activity).all()
	return activities

def query_activity_by_id(activity_id):
	activity=session.query(Activity).filter_by(activity_id=activity_id).first()
	return activity

def update_activity_volunteer(activity_id,volunteers):
	activity=session.query(Activity).filter_by(activity_id=activity_id).first()
	activity.volunteers=volunteers
	session.commit()

def update_activity_refugee(activity_id,refugees):
	activity=session.query(Activity).filter_by(activity_id=activity_id).first()
	activity.refugees=refugees
	session.commit

def signup_refugee(name, email, password, gender, age):
	refugee_object = Refugee(
		name=name,
		email=email,
		password=password,
		gender=gender,
		age=age)
	session.add(refugee_object)
	session.commit()

