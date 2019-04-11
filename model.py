from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Refugee(Base):
	__tablename__="refugees"
	refugee_id=Column(Integer,primary_key=True)
	name=Column(String)
	email=Column(String)
	password=Column(String)
	gender=column(String)
	age=column(String)

class Volunteer(Base):
	__tablename__="volunteers"
	volunteer_id=Column(Integer,primary_key=True)
	name=Column(String)
	email=Column(String)
	password=Column(String)
	gender=column(String)
	age=column(String)

class Story(Base):
	__tablename__="stories"
	story_id=Column(Integer,primary_key=True)
	name=Column(String)
	email=Column(String)
	age=column(String)
	content=column(String)

class Activty(Base):
	__tablename__="activities"
	activity_id=Column(Integer,primary_key=True)
	name=Column(String)
	description=Column(String)
	age=column(String)
	date=column(date)
	location=column(String)
	leader=Column(String)
	volunteers= column()