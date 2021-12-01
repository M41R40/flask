from flask import Blueprint, render_template

auths = Blueprint('auths', __name__)

@auths.route('login')
def login():
  return render_template('login.html', name='Gabriel Dornas', boolean=False)

@auths.route('logout')
def logout():
  return "<h1>Logout</h1>"

@auths.route('sign-up', methods=['GET', 'POST'])
def sign_up():
  return render_template('sign_up.html')
