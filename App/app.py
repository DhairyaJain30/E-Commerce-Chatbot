from flask import Flask, request, jsonify
from flask import render_template
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Loading env variables
load_dotenv()

app = Flask(__name__)
CORS(app)

RASA_API_URL = os.getenv("RASA_API_URL", "http://localhost:5005/webhooks/rest/webhook")

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    payload = {
        "sender": "user",         # Can be any ID
        "message": user_message
    }

    try:
        response = requests.post(RASA_API_URL, json=payload)
        bot_messages = response.json()
        reply = " ".join([msg.get("text", "") for msg in bot_messages])
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000, debug=True)
