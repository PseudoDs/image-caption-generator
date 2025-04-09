from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
from transformers import pipeline
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Load model at startup
model = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

@app.route('/', methods=['GET', 'POST'])
def home():
    caption = None
    filename = None
    
    if request.method == 'POST' and 'image' in request.files:
        file = request.files['image']
        if file.filename != '':
            # Save uploaded file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Generate caption
            image = Image.open(filepath)
            result = model(image)
            caption = result[0]['generated_text']
    
    return render_template('index.html', caption=caption, filename=filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)