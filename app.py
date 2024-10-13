from flask import Flask, request, render_template, jsonify
import os
import pickle
import numpy as np
from werkzeug.utils import secure_filename
from PIL import Image
import tensorflow as tf
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day", "10 per hour"]
)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 

# Load the model once during app startup
model = None
def load_model():
    global model
    if model is None:
        with open('deepfake_model.pkl', 'rb') as f:
            model = pickle.load(f)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    """Preprocess the image to the required input shape of the model."""
    img = Image.open(image_path)
    img = img.resize((224, 224))  
    img = np.array(img)
    
    if img.shape[-1] == 4: 
        img = img[..., :3]
    
    img = img / 255.0  
    img = np.expand_dims(img, axis=0)  
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
@limiter.limit("5 per minute")  
def upload_file():
    try:
       
        if 'file' not in request.files:
            return jsonify({"alert": "No file part"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"alert": "No selected file"}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            
            img = preprocess_image(filepath)

           
            load_model()  
            prediction = model.predict(img)[0][0]  

            # Determine if it's a real or fake based on the prediction
            if prediction < 0.5:
                result = "Real"
            else:
                result = "Fake"

            return jsonify({"alert": f"The image is {result} with a confidence of {prediction:.2f}"}), 200
        else:
            return jsonify({"alert": "Invalid file type"}), 400
    except Exception as e:
        return jsonify({"alert": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
