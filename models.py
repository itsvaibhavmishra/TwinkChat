from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from time import localtime, strftime

db = SQLAlchemy()

class User(UserMixin, db.Model): 	# UserMixin does not affect DB
	# User Model

	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(), unique = True, nullable = False)
	username = db.Column(db.String(25), unique = True, nullable = False)
	password = db.Column(db.String(), nullable = False)


class UserMes(UserMixin, db.Model):
	# Message Model
	__tablename__ = "usermes"
	id = db.Column(db.Integer, primary_key = True)
	room = db.Column(db.String(), nullable = False)
	username = db.Column(db.String(25), unique = True, nullable = False)
	messages = db.Column(db.String(), nullable = False)
	time = db.Column(db.DateTime(), default = strftime('%I:%M%p', localtime()))