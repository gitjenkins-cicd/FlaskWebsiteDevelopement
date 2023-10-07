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