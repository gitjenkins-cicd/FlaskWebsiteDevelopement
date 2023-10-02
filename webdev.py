from flask import Flask, render_template, request, views
from app import app
@app.route("/")
def helloworld():
    return render_template('home.html')

def upload():
    return render_template("home.html")