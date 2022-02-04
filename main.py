import uuid
import datetime
import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("tle-csis3126-firebase-adminsdk-8jeqr-3bc610acea.json")
firebase_admin.initialize_app(cred,
{
 "databaseURL": "https://tle-csis3126.firebaseio.com/"
})

db = firestore.client()
id = uuid.uuid1()

email = input('Please enter email')
password = input('Please enter password')

user = auth.create_user(email = email, password = password)
print("User created successfully : {0}".format(user.uid))


data = {
    u'humidity': .99,
    u'temperature': 87,
    u'user': u'911911',
    u'ts': datetime.datetime.now(tz=datetime.timezone.utc)
    }
db.collection(u'measurements').document(str(id)).set(data)