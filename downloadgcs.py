from flask import Flask, render_template, request, views, send_file
from google.cloud import storage
from app import app
@app.route('/downloadfile/filename', methods=['POST'])
def downloadfile(filename):
    bucket_name = 'imrantestbucket'
    source_blob_name = f'gs://imrantestbucket/{file_name}'
    temp_file_path = f'/tmp/{file_name}'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(temp_file_path)
    return send_file(temp_file_path, as_attachment=True, attachment_filename=file_name)



