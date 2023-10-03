from flask import Flask, render_template, request, views, send_file
from google.cloud import storage
from app import app
storage_client = storage.Client()
@app.route('/downloadfile/<filename>')
def downloadfile(filename):
    bucket_name = 'imrantestbucket'
    source_blob_name = f'gs://imrantestbucket/{filename}'
    temp_file_path = f'/tmp/{filename}'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(temp_file_path)
    return send_file(temp_file_path, as_attachment=True, attachment_filename=filename)



