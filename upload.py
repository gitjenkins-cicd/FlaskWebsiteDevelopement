from flask import Flask, render_template, request, views
from app import app
# @app.route("/")
# def helloworld():
#     return render_template('home.html')

# def upload():
#     return render_template("home.html")


@app.route('/uploadfile', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        # f.save(f.filename)
        f.save('D:/HotTechnologies/python/FlaskWebsiteDevelopement/files/' + f.filename)
        return render_template("success.html", name=f.filename)