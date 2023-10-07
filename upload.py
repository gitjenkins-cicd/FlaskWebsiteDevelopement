from flask import Flask, render_template, request, views
app=Flask(__name__)
from app import app
@app.route('/uploadfile', methods=['POST'])
def upload():
    if request.method == 'POST':
        files = request.files['file']
        # f.save(f.filename)
        files.save('d:/HotTechnologies/python/FlaskWebsiteDevelopement/files/'+ files.filename)
        return render_template("success.html", name=files.filename)