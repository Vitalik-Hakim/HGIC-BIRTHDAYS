import pyrebase

config = {
  "apiKey": "AIzaSyDjGYijrdvaOMXq26Lc2IS9OQKKL7D_KXI",
  "authDomain": "someprojectbi.firebaseapp.com",
  "projectId": "someprojectbi",
  "storageBucket": "someprojectbi.appspot.com",
  "messagingSenderId": "311803201634",
  "appId": "1:311803201634:web:c878ce2f7be0cba463e93b",
  "measurementId": "G-5RH59VY3QQ",
  "databaseURL":"https://someprojectbi-default-rtdb.firebaseio.com",
  "serviceAccount": "serviceKey.json"

}

firebase = pyrebase.initialize_app(config)


db = firebase.database()

users = db.child("April").get()
print(users.key())


