
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
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


# ///////////////////////////////
#Gallery

def add_image(path, title, content):
	image=Image(
		image_path=path,
		image_title=title,
		image_txt=content
	)
	session.add(image)
	session.commit()

def delete_image_by_id(id): #by id
	session.query(Image).filter(Image.image_id==id).delete()
	session.commit()

def delete_image_by_path(path):
	session.query(Image).filter(Image.image_path==path).delete()
	session.commit()

# ///////////////////////////////

def display_stories():
	stories=session.query(Story).all()
	
	return stories

def add_story(name,age,content,before,after):
	story=Story(name=name,age=age,content=content)
	session.add(story)
	session.commit()
	