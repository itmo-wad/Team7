from flask import Flask
from app import app
from user.models import User
#route that send the user to the signup page to tell the mongodb to add the user
@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()
#log out and end the user session
@app.route('/user/signout')
def signout():
  return User().signout()
#login the created user
@app.route('/user/login', methods=['POST'])
def login():
  return User().login()