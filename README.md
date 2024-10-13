# Deepfake Detection Web Application

This project is a web-based deepfake detection system where users can upload images, and the app will analyze them to determine if they are real or fake using a pre-trained deepfake detection model. The backend is built using Flask, and the frontend is developed with HTML, CSS, and JavaScript.

## Features
- **Image Upload**: Users can upload `.jpg`, `.jpeg`, or `.png` image files for analysis.
- **Deepfake Detection**: The system predicts whether an image is real or fake using a pre-trained machine learning model.
- **Real-Time Feedback**: Results are displayed on the same page dynamically using AJAX without reloading the entire page.
- **Rate Limiting**: To prevent abuse, the system limits the number of uploads a user can make within a certain time period.
  
## Project Structure
├── app.py # Flask application backend 
├── templates │ └── index.html # HTML file for frontend 
├── static │ └── style.css # CSS file for styling 
├── uploads # Directory for storing uploaded images 
├── deepfake_model.pkl # Pre-trained deepfake detection model 
└── README.md # Project documentation



## Requirements
To run this project, ensure you have the following installed:

### Dependencies
- **Flask**: Python web framework used to create the backend server.
- **Pillow**: Python library for image processing.
- **NumPy**: Python library for handling arrays and numerical data.
- **Werkzeug**: Provides utilities for handling file uploads securely.
- **TensorFlow**: Used for deep learning, to run the pre-trained deepfake detection model.
- **Flask-Limiter**: A Flask extension to implement rate limiting.

### Python Packages:
You can install the required packages using `pip`:

```bash
pip install Flask Pillow numpy werkzeug tensorflow Flask-Limiter
