import sys

sys.path.insert(0, 'Controller')
from db import *

app = Flask(__name__)

id = 0
@app.route("/")
def index():
	return render_template("login.html")
@app.route("/login",methods=['POST','GET'])
def login():
	return render_template("apology.html")
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
		new_ex = Users(username,password,None,None,None,email)
		id = new_ex.username
		db.session.add(new_ex)
		db.session.commit()
		return redirect(url_for('register_cont',username=username))
	else:
		return render_template("hack.html")

@app.route('/register_cont',methods=['POST','GET'])
def register_cont():
	if request.method == "POST":
		us = request.form.get("username")
		user = Users.query.filter_by(username=us).first()
		user.status=1
		user.name = request.form.get('nme')
		user.sname = request.form.get('sname')
		user.about = request.form.get('desc')
		month = request.form.get('DOBMonth')
		day = request.form.get('DOBDay')
		year = request.form.get('DOBYear')
		user.day_of_birth = day+"/"+month+"/"+year
		db.session.commit()
		return redirect(url_for("profile",username=user.username))
	if request.method == "GET":
		usernamee = request.args['username']
		return render_template("register_cont.html",user=usernamee)

@app.route("/profile/<username>")
def profile(username):
	return "OK"
	
''' Ajax section '''
@app.route("/get_users",methods=['POST'])
def get_users():
	query = Users.query.order_by(Users.username).all()
	return jsonify([e.jsn() for e in query])

