import pyrebase

config = {
  "apiKey": "AIzaSyBFj4WtVAfarJFy0V6YwccqTNplYajofOo",
  "authDomain": "ytconvert-f92e2.firebaseapp.com",
  "databaseURL": "",
  "storageBucket": "ytconvert-f92e2.appspot.com",
  "appId": "1:479741046984:web:5e86d7729e55b5760ab5fd",
  "measurementId": "G-DSWWEJCHDT"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()



