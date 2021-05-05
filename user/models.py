from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid

# models to populate the mongodb collections
class User:
# self: access the attributes and methods of the class, 
# It binds the attributes with the given arguments (user)
  def start_session(self, user):
    # delete passowrd from the session value for security
    del user['password']
    # session is a built in flask function
    session['logged_in'] = True #default vale true for the if condition usages
    # user data is converted to a specific session value that belong to the user
    session['user'] = user
    # return the user session with code 200 (success)
    return jsonify(user), 200

  def signup(self):
    print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password')
    }

    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      # if exist, return error with code 400
      return jsonify({ "error": "Email address already in use" }), 400
    # if not exist, create new user and assign session
    if db.users.insert_one(user):
      return self.start_session(user)
    # else for whatever reason, return error
    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    #clear the session
    session.clear()
    #return to the main page (sign up form)
    return redirect('/')
  
  def login(self):
    # query a user from db with the same email of the input form
    user = db.users.find_one({
      #DB email == user input email
      "email": request.form.get('email')
    })
    # check if the email and password of user input are the same in DB
    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      # if yes, start the session with theses values
      return self.start_session(user)
    # else return error
    return jsonify({ "error": "Invalid login credentials" }), 401