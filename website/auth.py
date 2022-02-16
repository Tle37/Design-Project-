from flask import Blueprint, render_template, request, flash

import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("tle-csis3126-firebase-adminsdk-8jeqr-3bc610acea.json")
firebase_admin.initialize_app(cred,
{
 "databaseURL": "https://tle-csis3126.firebaseio.com/"
})

db = firestore.client()

auth = Blueprint('auth', __name__)


@auth.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        auth.sign_in_with_email_and_password.get(email, password)
    return render_template("login.html")



@auth.route('/sign-up',methods =['GET','POST'])
def sign_up():
    if request.method == 'POST':
     email = request.form.get('email')
     firstName = request.form.get('firstName')
     password1 = request.form.get('password1')
     password2 = request.form.get('password2')
     if len(email) < 4:
         flash('Email is invalid.', category='error')
     elif len(firstName) < 1:
         flash('First name is must be greater than one character.', category='error')
     elif len(password1) != password2:
         flash('Passwords do not match!.', category='error')
     elif len(password1) < 7:
         flash('Password must be more than 7 characters.', category='error')
     else:
         flash('Account created!', category='success')
    return render_template("sign_up.html")

@auth.route('/logout')
def logout():
    return
