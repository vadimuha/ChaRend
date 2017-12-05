from flask import Flask,render_template,request,jsonify,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  and_, or_
import hashlib,time,random

app = Flask(__name__)

app.secret_key = str(random.randint(0,9999999))
