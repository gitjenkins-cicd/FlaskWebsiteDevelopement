from flask import Flask, render_template, request, views, send_file
from google.cloud import storage
app=Flask(__name__)
from app import app
@app.route('/uploadfile', methods=['POST'])
def upload():
    if request.method == 'POST':
        files = request.files['file']
        # f.save(f.filename)
        files.save('d:/HotTechnologies/python/FlaskWebsiteDevelopement/files/'+ files.filename)
        return render_template("success.html", name=files.filename)
    
@app.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get('filename')
    try:
        file_path = f'D:/HotTechnologies/python/FlaskWebsiteDevelopement/files/{filename}'  # Replace with the actual file path
        print(file_path)
        return send_file(file_path, as_attachment=True ) 
        # render_template('downloadfile.html')
    except FileNotFoundError:
        return "File not found."


client = storage.Client()
@app.route('/downloadgcs', methods=['POST'])
def download_gcsfile():
    files = request.form['filename']
    bucket_name = 'imrantestbucket'  # Replace with your GCS bucket name

    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(files)
        blob.download_to_filename(files)
        return send_file(files, as_attachment=True)
    except Exception as e:
        return str(e)

# from flask_mysqldb import MySQL
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'redhat'
# app.config['MYSQL_DB'] = 'mysql'
# mysql = MySQL(app)

# @app.route('/db')
# def index():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM user')
#     if cur is None:
#         return "Failed to establish a database connection."
#     data = cur.fetchall()
#     cur.close()
#     return render_template('index.html', user=data)


from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:redhat@localhost/mysql'
db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'


@app.route('/db')
def index():
    result = db.engine.execute('SELECT User, Host, authentication_string FROM user')
    users = [dict(row) for row in result]
    # print(Host)
    # user1=[row for row in users]
    # print(user1)
    return render_template('index.html', users=users)

import pandas as pd
@app.route('/analyze', methods=['POST'])
def analyze():
    csv_file = request.files['csv_file']
    df = pd.read_csv(csv_file, low_memory=False)
    mean = df.mean()
    median = df.median()
    std_dev = df.std()
    max_value = df.max()
    min_value = df.min()
    summary_stats = df.describe()

    return render_template('csvresults.html', summary_stats=summary_stats, mean=mean, 
                           median=median, 
                           std_dev=std_dev, 
                           max_value=max_value, 
                           min_value=min_value)