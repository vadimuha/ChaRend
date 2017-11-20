import sys

sys.path.insert(0, 'Controller')
from db import *

app = Flask(__name__)


app.secret_key = str(random.randint(0,9999999))

@app.route("/")
def index():
	try:
		session['user']
		return redirect(url_for("profile",username=session['user']))
	except KeyError:
		return render_template("login.html")

@app.route("/login",methods=['POST','GET'])
def login():
	login = request.form.get("email")
	password = request.form.get("password")
	password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
	query = Users.query.all()
	jsn = [e.jsn() for e in query]
	for i in jsn:
		if login == i["username"] or login == i["mail"]:
			if password == i["passwd"]:
				session["user"] = i['username']
				return redirect(url_for("profile"))

	return render_template("hack.html")

@app.route("/register",methods=['POST','GET'])
def register():
	if request.method == "POST":
		username = request.form.get("username")
		email = request.form.get("email")
		password = request.form.get("pass")
		re_password = request.form.get("re-pass")
		if password != re_password:
			return render_template("hack.html")
		query = Users.query.order_by(Users.username).all()
		users = [e.jsn() for e in query]
		if username in users:
			return render_template("hack.html")
		password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
		new_ex = Users(username,password,None,None,None,email)
		id = new_ex.username
		db.session.add(new_ex)
		db.session.commit()
		return redirect(url_for('register_cont',username=username) )
	else:
		return render_template("hack.html")

@app.route('/register_cont',methods=['POST','GET'])
def register_cont():
	if request.method == "POST":
		us = request.form.get("username")
		user = Users.query.filter_by(username=us).first()
		user.status=1
		user.name = request.form.get('nme')
		user.surname = request.form.get('sname')
		user.about = request.form.get('desc')
		month = request.form.get('DOBMonth')
		day = request.form.get('DOBDay')
		year = request.form.get('DOBYear')
		user.day_of_birth = day+"/"+month+"/"+year
		db.session.commit()
		session['user'] = user.id
		return redirect(url_for("profile",username=user.username))
	
	if request.method == "GET":
		usernamee = request.args['username']
		return render_template("register_cont.html",user=usernamee)

@app.route("/profile/<username>")
def profile(username):
	query = Users.query.filter_by(username=username).first()
	

	return render_template("profile.html",username=username,name=query.name,sname=query.surname,desc=query.about)

''' Ajax section '''
@app.route("/check_username_existence",methods=['GET'])
def check_username_existence():
	query = Users.query.order_by(Users.username).all()
	jsn = [e.jsn() for e in query]
	usr = request.args.get("username")
	for i in jsn:
		if(usr == i["username"]):
			return '1'
	return '0'

@app.route("/check_login",methods=['GET'])
def check_login():
	log = request.args.get("login")
	paswd = request.args.get("password")
	query = Users.query.all()
	jsn = [e.jsn() for e in query]

	pl = 0
	for i in jsn:
		if log == i["username"] or log == i["mail"]:
			pl = 1
			if paswd == i["passwd"]:
				pl = 1
			else:
				pl = 0
	if pl:
		return "1"
	else:
		return "0"

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)