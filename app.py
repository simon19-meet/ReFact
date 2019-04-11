from flask import Flask, render_template, url_for, redirect, request
from database import *
from flask import session as login_session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)



if __name__ == '__main__':
	app.run(debug=True)

