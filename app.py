from flask import Flask, flash, request, redirect, url_for, render_template
from rembg import remove
import os
import random
import pyrebase
from dotenv import load_dotenv

load_dotenv()
firebase_api_key = os.getenv("FIREBASE_API_KEY")
print(firebase_api_key)
config = {
  "apiKey": firebase_api_key,
  "authDomain": "flask-firebase-storage.firebaseapp.com",
  "databaseURL": "",
  "storageBucket": "flask-firebase-storage.appspot.com",
  "appId": "1:670694688551:web:d627e473ec0bce9112cb02",
  "measurementId": "G-DSWWEJCHDT"
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template("index.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST': 
        img = request.files['image']
        oname = os.path.join("static/results/", img.filename)
        input = img.read()
        output = remove(input)
        imgurl = storage.child("static/results/" + img.filename).put(output)
        url = storage.child("static/results/" + img.filename).get_url(imgurl['downloadTokens'])
        return url
    return 'Wrong Request'

if __name__ == '__main__' :
    app.run(debug=True)