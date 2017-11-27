from config import *

app = Flask(__name__)	# I don't know why but it does not work without it

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class Users(db.Model):
	__tablename__ = "users"
	id = db.Column("id",db.Integer,primary_key=True)
	username = db.Column("username",db.Unicode,unique=True)
	passwd = db.Column("pass",db.Unicode)
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

	def jsn(self):	# Custom jsoify func (dictonify)
		return {
			"username": self.username,
			"passwd": self.passwd,
			"mail": self.email,
			"name": self.name,
			"surname": self.surname,
			"about": self.about,
			"day_of_birth": self.day_of_birth,
			"id": self.id,
			"status": self.status,
			"img": self.img
		}
class Statistics(db.Model):
	__tablename__ = "statistics"
	id = db.Column("id",db.Integer,primary_key=True)
	user_id = db.Column("user_id",db.Integer,db.ForeignKey("users.id"))
	times_online = db.Column("times_online",db.Integer)
	sent_messages = db.Column("sent_messages",db.Integer)

	def __init__(self,user_id):
		self.times_online = user_id
		self.sent_messages = 0
		self.user_id = 0
