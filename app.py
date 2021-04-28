from flask import Flask, render_template, session, redirect, request
from functools import wraps
import pymongo
import random
import string
import csv
import json

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes
from user import routes

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/dashboard/',  methods=['GET', 'POST'])
@login_required
def dashboard():
  if request.method == 'POST':
    results = []
      
    user_csv = request.form.get('user_csv').split('\n')
    reader = csv.DictReader(user_csv, delimiter = ';')
      
    for row in reader:
      results.append(dict(row))

    fieldnames = [key for key in results[0].keys()]

    return render_template('dashboard.html', results=results, fieldnames=fieldnames, len=len)

  elif request.method == 'GET':
    return render_template('dashboard.html')


@app.route('/info <row>')
def info(row):
   str = row.replace("\'", "\"")
   Diction = eval(str)
   return render_template('info.html', rowDic = Diction)



