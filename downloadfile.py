from flask import Flask, send_file, request, render_template
app=Flask(__name__)
from app import app
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
    
