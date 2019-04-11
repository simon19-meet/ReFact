
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def signup_refugee(name, email, password, gender, age):
	refugee_object = Refugee(
		name=name,
		email=email,
		password=password,
		gender=gender,
		age=age)
	session.add(refugee_object)
	session.commit()

def signup_volunteer(name, email, password, gender, age):
	volunteer_object = Volunteer(
		name=name,
		email=email,
		password=password,
		gender=gender,
		age=age)
	session.add(volunteer_object)
	session.commit()

