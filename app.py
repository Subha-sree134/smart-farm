from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Home Route (Loads the Website)
@app.route('/')
def home():
    return render_template('index.html')

# Upload Image Route (Handles Image Uploads)
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    return jsonify({'message': 'File uploaded successfully', 'filename': filename})

# Get Market Prices Route (Sends Crop Prices as JSON)
@app.route('/market-prices')
def get_market_prices():
    market_data = {
        "Wheat": "$5 per kg",
        "Rice": "$4 per kg",
        "Corn": "$3 per kg"
    }
    return jsonify(market_data)

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)