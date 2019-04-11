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
	gender=column(string)
	age=column(string)

class Volunteer(Base):
	__tablename__="volunteers"
	volunteer_id=Column(Integer,primary_key=True)
	name=Column(String)
	email=Column(String)
	password=Column(String)
	gender=column(string)
	age=column(string)