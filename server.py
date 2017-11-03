from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("registration.html")
@app.route("/login",methods=['POST','GET'])
def login():
	return render_template("apology.html")
@app.route("/register",methods=['POST','GET'])
def register():
	return render_template("apology.html")