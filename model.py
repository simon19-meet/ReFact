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

# ////////////////////////////////////////////////////////////////////////////////////////////////////////


class Gallery(Base):
	__tablename__="Gallery"
	image_id=Column(Integer, primary_key=True)
	image_path=Column(String)
	image_title=Column(String)
	image_txt=Column(Text)
	

# ////////////////////////////////////////////////////////////////////////////////////////////////////////	