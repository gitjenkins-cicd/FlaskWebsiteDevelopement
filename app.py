from flask import Flask, render_template, request, session
app=Flask(__name__)
from downloadfile import *
from upload import *
from webdev import *
from downloadgcs import *
from downloadfile import *
from login import *

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)