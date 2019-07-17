from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,PickleType, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Feedback(Base):
	__tablename__="feedbacks"
	feedback_id=Column(Integer,primary_key=True)
	name=Column(String)
	age=Column(String)
	content=Column(Text)

class Volunteer(Base):
	__tablename__="volunteers"
	volunteer_id=Column(Integer,primary_key=True)
	name=Column(String)
	email=Column(String)
	gender=Column(String)
	age=Column(String)
	number=Column(String)
	address=Column(String)
	work=Column(String)
	academic_level=Column(String)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////


class Image(Base):
	__tablename__="Gallery"
	image_id=Column(Integer, primary_key=True)
	image_path=Column(String)
	image_title=Column(String)
	image_txt=Column(Text)
	

# ////////////////////////////////////////////////////////////////////////////////////////////////////////	
