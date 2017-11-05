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
	user = request.args['username']
	query = Users.query.filter_by(username=user).first()
	print(query.id)
	return render_template("register_cont.html")

''' Ajax section '''
@app.route("/get_users",methods=['POST'])
def get_users():
	query = Users.query.order_by(Users.username).all()
	return jsonify([e.jsn() for e in query])

