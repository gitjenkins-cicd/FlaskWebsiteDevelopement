from flask import Flask, send_file, request, render_template
from app import app
@app.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get('filename')
    try:
        file_path = f'D:/HotTechnologies/python/FlaskWebsiteDevelopement/files/{filename}'  # Replace with the actual file path
        return send_file(file_path, as_attachment=True) 
        # return render_template("downloadfile.html")
        # return render_template("downloadfile.html", name=filename)
    except FileNotFoundError:
        return "File not found."