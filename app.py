from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import datetime
import random

app = Flask(__name__)
CORS(app)

CLIMATS = ["☀️", "🌤️", "🌦️", "🌧️", "🌫️", "🌩️"]
OISEAUX = ["🕊️", "🐥", "🐦", "🐧", "🦉", "🦅"]
MOODS = {
    "☀️": ["😄", "😊", "😀"],
    "🌤️": ["😌", "🙂", "😏"],
    "🌦️": ["😐", "😶", "😕"],
    "🌧️": ["😟", "😢", "🙁"],
    "🌫️": ["😣", "😷", "🤧"],
    "🌩️": ["😫", "😱", "😨"]
}

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/api/v1/birdfeedback', methods=['GET'])
def BirdFeedbackAPI():
    climat = random.choice(CLIMATS)
    mood_list = MOODS[climat]
    mood = random.choice(mood_list)
    oiseau_dominant = random.choice(OISEAUX)

    timestamp = datetime.datetime.now(datetime.UTC).isoformat()

    return jsonify({
        "timestamp": timestamp,
        "climat": climat,
        "mood": mood,
        "oiseau": oiseau_dominant
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
