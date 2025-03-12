from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

# Define data folder path
DATA_FOLDER = os.path.join(os.path.dirname(__file__), 'data')
TEMPLATE_FOLDER = os.path.join(os.path.dirname(__file__), 'templates')

# Route to serve the main dashboard
@app.route("/")
def index():
    return render_template('index.html')

# API endpoint for marketShare.json
@app.route("/api/marketShare")
def get_market_share():
    filepath = os.path.join(DATA_FOLDER, 'marketShare.json')
    with open(filepath, 'r') as f:
        data = json.load(f)
    return jsonify(data)

# API endpoint for revenueTrends.json
@app.route("/api/revenueTrends")
def get_revenue_trends():
    filepath = os.path.join(DATA_FOLDER, 'revenueTrends.json')
    with open(filepath, 'r') as f:
        data = json.load(f)
    return jsonify(data)

# API endpoint for marketSegmentation.json
@app.route("/api/marketSegmentation")
def get_market_segmentation():
    filepath = os.path.join(DATA_FOLDER, 'marketSegmentation.json')
    with open(filepath, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
