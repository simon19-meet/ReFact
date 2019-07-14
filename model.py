from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Feedback(Base):
	__tablename__="feedbacks"
	feedback_id=Column(Integer,primary_key=True)
	name=Column(String)
	age=Column(String)
	content=Column(String)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

class Activity(Base):
	__tablename__="activities"
	activity_id=Column(Integer,primary_key=True)
	name=Column(String)
	description=Column(String)
	age=Column(String)
	date=Column(String)
	location=Column(String)
	leader=Column(String)
	volunteers=Column(String)

class Refugee(Base):
	__tablename__="refugees"
	refugee_id=Column(Integer,primary_key=True)
	name=Column(String)
	email=Column(String)
	password=Column(String)
	gender=Column(String)
	age=Column(String)

class Volunteer(Base):
	__tablename__="volunteers"
	volunteer_id=Column(Integer,primary_key=True)
	name=Column(String)
	email=Column(String)
	password=Column(String)
	gender=Column(String)
	age=Column(String)
