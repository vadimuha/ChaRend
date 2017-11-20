from flask import Flask,render_template,request,jsonify,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
import hashlib,time,random

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Users(db.Model):
	__tablename__ = "users"
	id = db.Column("id",db.Integer,primary_key=True)
	username = db.Column("username",db.Unicode,unique=True)
	passwd = db.Column("passwd",db.Unicode)
	status = db.Column("status",db.Integer)
	name = db.Column("name",db.Unicode)
	surname = db.Column("surname",db.Unicode)
	about = db.Column("about",db.Unicode)
	email = db.Column("email",db.Unicode)
	day_of_birth = db.Column("day_of_birth",db.Unicode)
	img = db.Column("img",db.Unicode)
	def __init__ (self,username,passwd,name,surname,about,email,status):
		self.username = username
		self.passwd = passwd
		self.status = 0
		self.name = name
		self.surname = surname
		self.about = about
		self.email = email
		self.status = status
	def jsn(self):
		return {
			"username": self.username,
			"passwd": self.passwd,
			"mail": self.email,
			"name": self.name,
			"surname": self.surname,
			"about": self.about,
			"day_of_birth": self.day_of_birth,
			"id": self.id,
			"status": self.status
		}

class Groups(db.Model):
	id = db.Column("id",db.Integer,primary_key=True)
	name = db.Column("name",db.Unicode,unique=True)
	def __init__(self,name):
		self.name = name