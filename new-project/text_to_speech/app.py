from flask import Flask, request, send_file
import requests
import io
import os

app = Flask(__name__)

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")  # Replace this with your ElevenLabs API Key
VOICE_ID = '21m00Tcm4TlvDq8ikWAM'  # Default voice, or use another from your account

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    text = data.get('text', '')

    headers = {
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Type': 'application/json'
    }

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(
        f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}',
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        return 'Error from ElevenLabs', 500

    return send_file(
        io.BytesIO(response.content),
        mimetype='audio/mpeg',
        as_attachment=False,
        download_name='speech.mp3'
    )

if __name__ == '__main__':
    app.run(debug=True)
