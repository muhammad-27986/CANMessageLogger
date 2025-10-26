from flask import Flask, jsonify
from flask_cors import CORS
import json, random

app = Flask(__name__)
CORS(app)

@app.route("/data")
def get_data():
    try:
        with open("dashcam_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return jsonify({"speed":0,"rpm":0,"fuel":0,"temperature":0})

    if not data:
        return jsonify({"speed":0,"rpm":0,"fuel":0,"temperature":0})

    entry = random.choice(data)
    return jsonify(entry)

if __name__ == "__main__":
    app.run(debug=True)
