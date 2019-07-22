from flask import Flask, render_template, url_for, redirect, request
from database import * 	
from flask import session as login_session
from os import environ
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_mail import Mail, Message ##mail api

app=Flask(__name__)
mail = Mail(app)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'refact.meet@gmail.com',
    "MAIL_PASSWORD": 'spreadjoyinspirehope'
}

app.config.update(mail_settings)
mail = Mail(app)
@app.route('/')
def send_bulk():
    subs= get_all_subs()
    with mail.connect() as conn:
        for sub in subs:
            message = 'Test'
            subject = "hello, %s" % sub.name
            msg = Message(recipients=[sub.email],
                        sender=app.config.get("MAIL_USERNAME"),
                        body=message,
                        subject=subject)

        conn.send(msg)
    return "sent."

if __name__ == '__main__':
	app.run(debug=True)




