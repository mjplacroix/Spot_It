from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "SpaceX launch today!!!"

@app.route("/about")

def preds():
    return render_template('home.html')