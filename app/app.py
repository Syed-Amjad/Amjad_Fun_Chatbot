from flask import Flask, render_template, request, jsonify
from chatbot import process_input
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("input")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    response_text, response_audio_path = process_input(user_input)
    return jsonify({"text": response_text, "audio": response_audio_path})

if __name__ == "__main__":
    app.run(debug=True)
