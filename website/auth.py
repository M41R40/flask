from flask import Blueprint, render_template, request

auths = Blueprint('auths', __name__)

@auths.route('login', methods=['GET', 'POST'])
def login():
  data = request.form
  print(data)
  return render_template('login.html')

@auths.route('logout')
def logout():
  return "<h1>Logout</h1>"

@auths.route('sign-up', methods=['GET', 'POST'])
def sign_up():
  data = request.form
  print(data)
  return render_template('sign_up.html')
