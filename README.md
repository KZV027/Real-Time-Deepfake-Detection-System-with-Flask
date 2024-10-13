# Deepfake Detection Web Application

This is a Flask-based web application that allows users to upload an image and detect if it is a deepfake or not. The app utilizes a pre-trained deepfake detection model and provides real-time results, indicating whether the uploaded image is classified as "Real" or "Fake" along with the confidence level.

## Features

- **Deepfake Detection**: Users can upload an image in `.jpg`, `.jpeg`, or `.png` format, and the app will classify it as either "Fake" or "Real".
- **Rate Limiting**: Limits users to 5 uploads per minute to prevent abuse.
- **File Upload**: A simple user interface allows for easy file uploads and viewing results directly in the browser.
- **Redis-Backed Limiting**: Uses Redis for efficient request limiting.
- **Responsive UI**: Features a clean, user-friendly interface.

## Project Structure

```bash
deepfake-detection-app/
│
├── app.py                  # Main Flask app
├── templates/
│   └── index.html           # Frontend HTML page
├── uploads/                 # Folder for storing uploaded images
├── static/                  # Static files (if any)
├── deepfake_model.pkl       # Pre-trained deepfake detection model
└── README.md                # Project documentation
```



## Technologies Used
* **Flask:** Backend web framework for handling requests.
* **TensorFlow:** For loading and utilizing the deepfake detection model.
* **Redis:** Used for rate-limiting.
* **HTML/CSS:** Frontend for the user interface.
* **Pickle:** To load the deepfake detection model.
* **Werkzeug:** To securely handle file uploads.
* **PIL (Pillow):** For image processing.

## Requirements
To run this project, ensure you have the following installed:

## Dependencies
* **Flask:** Python web framework used to create the backend server.
* **Pillow:** Python library for image processing.
* **NumPy:** Python library for handling arrays and numerical data.
* **Werkzeug:** Provides utilities for handling file uploads securely.
* **TensorFlow:** Used for deep learning, to run the pre-trained deepfake detection model.
*  **Flask-Limiter:** A Flask extension to implement rate limiting.

## Python Packages
You can install the required packages using ```pip```:
```bash
pip install Flask Pillow numpy werkzeug tensorflow Flask-Limiter redis
```
## Redis Installation
If Redis is not already installed, follow the steps to install and start the Redis server:
```bash
sudo apt-get install redis-server
sudo service redis-server start
``` 
## How to Run the App
1. Clone the repository:
```bash
git clone https://github.com/yourusername/deepfake-detection-app.git
cd deepfake-detection-app

``` 

2. Install dependencies:

Install the required Python packages listed in ```requirements.txt```:
```bash
pip install -r requirements.txt
``` 
3. Run the Redis server:

Ensure Redis is up and running on your machine:
```bash
redis-server
``` 
4.Run the Flask app:

Start the Flask development server:
```bash
python app.py
``` 
5. Access the web app:

Open your browser and go to ``` http://127.0.0.1:5000/```. 

## Usage
1. Open the app in your browser.
2. Upload a ```.jpg```, ```.jpeg```, or ```.png``` image.
3. Click on the "Detect" button to get the result.
4. The app will display whether the uploaded image is classified as "Real" or "Fake" along with the confidence score.
## Model
The deepfake detection model is pre-trained and saved as ```deepfake_model.pkl```. It processes input images of size ```224x224``` pixels and predicts whether they are real or fake. If the model’s prediction confidence is below 0.7, the image is classified as "Fake"; otherwise, it is classified as "Real".

## Limitations
* The model may not be 100% accurate and might require further fine-tuning for better results.
* The current version of the app is limited to detecting deepfakes in images. Future versions could include video detection.
## Future Improvements
* **Video Support:** Extend the model to detect deepfakes in video files.
* **Enhanced UI:** Improve the design and interactivity of the user interface.
* **Model Accuracy:** Train on larger datasets for improved accuracy.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.

