import os
from dotenv import load_dotenv
from transformers import pipeline
import requests
from gtts import gTTS

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Load Whisper Model
whisper_model = pipeline("automatic-speech-recognition", model="openai/whisper-small")

def process_input(user_input):
    # Process with Gemini API
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    response = requests.post("https://api.gemini.com/v1/chat", json={"message": user_input}, headers=headers)
    response_data = response.json()
    response_text = response_data.get("text", "Sorry, I didn't understand that.")
    
    # Convert Text-to-Speech
    tts = gTTS(response_text)
    audio_path = "static/response.mp3"
    tts.save(audio_path)

    return response_text, audio_path
