from flask import Flask, render_template, request
app=Flask(__name__)
from upload import *
from webdev import *


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)