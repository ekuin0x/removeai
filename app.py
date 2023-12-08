from flask import Flask, flash, request, redirect, url_for, render_template
from rembg import remove
from fire import storage

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template("index.html")

@app.route('/data', methods = ['POST'])
def data():
    if request.method == 'POST': 
        img = request.files['file']
        name = "(no_background)" + img.filename
        i = remove(img.read())
        storage.child(name).put(i)
        url = storage.child(name).get_url("")
        return url     
    
    return "PROBLEM OCCURED"

if __name__ == '__main__' :
    app.run(port=5000,debug=True)
