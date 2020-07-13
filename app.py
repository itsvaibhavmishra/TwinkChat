# Modules
import os
from time import localtime, strftime
from flask import Flask, render_template, url_for, redirect, flash
from passlib.hash import pbkdf2_sha256
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import json

# local files
from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)

app.secret_key = os.environ.get('TWINKSECRET')

# Configure DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# Initialize Flask-SocketIO
socketio = SocketIO(app)
ROOMS = ["GlobalChat", "Coders", "CyberTech", "Gamers", "News"]


# Configure flask login
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):

	return User.query.get(int(id))	# same as filter_by method


@app.route("/", methods = ['GET', 'POST'])
def index():

	return render_template("index.html")


@app.route("/signup", methods = ['GET','POST'])
def signup():

	# Updates DB if validation is success
	reg_form = RegForm() 	# from wtform_fields
	if reg_form.validate_on_submit():
		email = reg_form.email.data
		username = reg_form.username.data
		password = reg_form.password.data

		# Hashing password
		hashed_pswd = pbkdf2_sha256.hash(password)  	# default adds 16byte salt and 29k iterations

		# Add user
		user = User(email = email, username = username, password = hashed_pswd)
		db.session.add(user)
		db.session.commit()

		flash('Registration Complete. Please login.', 'success')
		return redirect(url_for('login'))

	return render_template("signup.html", form = reg_form)


@app.route("/login", methods = ['GET','POST'])
def login():

	login_form = LoginForm()

	# Allow Login if validation success
	if login_form.validate_on_submit():
		user_object = User.query.filter_by(username = login_form.username.data).first()
		login_user(user_object)
		return redirect(url_for('chat'))

	return render_template("login.html", form = login_form) 

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route("/chat", methods = ['GET', 'POST'])
#@login_required
def chat():

	# login_required can also be used instead of this if statement
	if not current_user.is_authenticated:
		flash('Unauthorised Access!. Please Login First', 'authError')
		return redirect(url_for('login'))

	
	return render_template('chat.html', username = current_user.username, rooms = ROOMS)

@app.route("/logout", methods = ['GET'])
def logout():

	logout_user()
	flash('Logged Out Successfully', 'success')
	return redirect(url_for('login'))

@app.route("/contact")
def contact():
	# Direct to contact developer page
	return render_template('contact.html')

@socketio.on('message')
def messsage(data):
	
	print(f"\n\n{data['room']}\n\n")
	send({'msg': data['msg'], 'username': data['username'], 'time_stamp': strftime('%I:%M%p', localtime())}, room = data['room'])

@socketio.on('join')
def join(data):

	join_room(data['room'])

	send({'msg': data['username'] + " has joined " + data['room']}, room = data['room'])


@socketio.on('leave')
def leave(data):

	leave_room(data['room'])
	send({'msg': data['username'] + " has left " + data['room']}, room = data['room'])

if __name__ == '__main__':

	app.run()
	