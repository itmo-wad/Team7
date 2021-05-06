from flask import Flask, render_template, session, redirect, request, url_for
from functools import wraps
import pymongo
import random
import string
import csv
import json


#setting the flask app name as "app"
app = Flask(__name__)
#flask secret key (binary random string: print(os.ranodm) to manage sessions for users
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Local Database connection
# client = pymongo.MongoClient('localhost', 27017)
# db = client.user_login_system

#Mongodb Atlas for Heroku connection

client = pymongo.MongoClient("mongodb+srv://testuser:testpassword@cluster0.dtngb.gcp.mongodb.net/q4u?retryWrites=true&w=majority")
db = client.test


















# Decorators: verify if the user currently logged in
# *args: variable length arguments (1,2,3,4....etc)
# variable length of keyword arguments (a:1,b:2,:c:3)
# f: the route function as an argument
#logged_in is the seesion value that is created earlier
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  # return the route function to direct the user to the destination page
  return wrap

# Routes
from user import routes

#rendering the sign in home page
@app.route('/')
def home():
  return render_template('home.html')


#rendering the csv convertion page
@app.route('/dashboard/',  methods=['GET', 'POST'])
@login_required
def dashboard():
  if request.method == 'POST':
    # reults is an empty list to store the csv in as dictionaries
    results = []
    # grap the csv file from the text area
    user_csv = request.form.get('user_csv').split('\n')
    #read the csv file as a dictionary seperated by semicolon
    reader = csv.DictReader(user_csv, delimiter = ';')
    # append eact row in the csv file as a dictionary elemnt inside the list
    for row in reader:
      results.append(dict(row))
    # assign the first dictionary (the first row in the csv file) as the fieldnames for the table
    fieldnames = [key for key in results[0].keys()]
    # render the list of dictionaries to be viewd in the html table
    print(results)
    return render_template('dashboard.html', results=results, fieldnames=fieldnames, len=len )
  # if there is no user input then render the page only
  elif request.method == 'GET':
    return render_template('dashboard.html')

#route to transfer the sudent data that came from his/her clicked row and viewed privatly
#the <row> argument is the string that contain the student data passd by the url_for in the html template
@app.route('/info <row>', methods=['GET', 'POST'])
def info(row):

  #replase each single quotation (') mark with double quotation mark
  #because the dictionar must be enclosed with double quotation(") mark
  #the "\'" stands for the single quotation mark and the \ is an escape character so the
  #python interpreter can recognize the ' from the " " that is ued in the built in function eval("")

  str = row.replace("\'", "\"")
  # convert the double quoted string to a dictionary so the for loop in the info template can iterate it
  Diction = eval(str)

  #return the newly converted dictionary to the info page so it can be viewed as a table
  return render_template('info.html', rowDic = Diction)
