        # app.py
from flask import Flask, jsonify

from flask_cors import CORS

from waitress import serve

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes



@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=7002)