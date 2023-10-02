from flask import Flask, render_template, request
app=Flask(__name__)
@app.route("/")
def helloworld():
    return render_template('home.html')

def upload():
    return render_template("home.html")


@app.route('/uploadfile', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        # f.save(f.filename)
        f.save('D:/HotTechnologies/python/FlaskWebsiteDevelopement/files/' + f.filename)
        return render_template("success.html", name=f.filename)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)