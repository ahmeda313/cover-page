from flask import Flask, request, render_template, send_file, jsonify
from flask_cors import CORS
import os
from utils.process_docx import extract_text
from utils.generate_cover import generate_insights

app = Flask(__name__)

CORS(app)

# Configure upload and output directories
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


@app.route('/upload', methods=['POST','GET'])
def upload_file():
    if 'file' not in request.files:
        print("no file found")
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        print("no file found")
        return "No selected file", 400
    
    if file and file.filename.endswith('.docx'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        text = extract_text(file_path)


        # Process the document
        result = generate_insights(text)
        
        return jsonify(result), 200
    else:
        return "Invalid file type. Only .docx files are allowed.", 400

if __name__ == '__main__':
    app.run(debug=True)
