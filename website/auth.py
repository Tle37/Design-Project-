from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
 return "<p>Login</p>"

@auth.route('/logout')
def logout():
 return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
 return "<p>Sign Up</p>"



#import firebase_admin
#from firebase_admin import credentials, firestore, auth
#cred = credentials.Certificate("tle-csis3126-firebase-adminsdk-8jeqr-3bc610acea.json")
#firebase_admin.initialize_app(cred,
#{
 #"databaseURL": "https://tle-csis3126.firebaseio.com/"
#})

#email = input('Please enter email')
#password = input('Please enter password')

#user = auth.create_user(email = email, password = password)
#print("User created successfully : {0}".format(user.uid))