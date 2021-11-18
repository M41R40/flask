from flask import Blueprint

auths = Blueprint('auths', __name__)

@auths.route('login')
def login():
  return "<h1>Login</h1>"

@auths.route('logout')
def logout():
  return "<h1>Logout</h1>"

@auths.route('sign-up')
def sign_up():
  return "<h1>Sign-up</h1>"
