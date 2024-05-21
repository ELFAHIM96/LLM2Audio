from flask import Flask, request, jsonify
from elevenlabs.client import ElevenLabs
from elevenlabs import play, stream
from langchain_community.llms import Ollama
import os

app = Flask(__name__)

# Initialize ElevenLabs and Ollama
client = ElevenLabs()
cached_llm = Ollama(model="llama3")

@app.route('/llm', methods=['POST'])
def ask():
    data = request.json
    query = data.get('query', '')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        # Generate and stream the initial response
        initial_audio_stream = client.generate(text="you asked " + query, stream=True)
        stream(initial_audio_stream)

        # Get response from cached_llm
        response_text = cached_llm.invoke(query)

        # Generate and stream the final response
        final_audio_stream = client.generate(text=response_text, stream=True)
        stream(final_audio_stream)

        return jsonify({"response": response_text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/play', methods=['POST'])
def play_audio():
    data = request.json
    text = data.get('text', '')
    voice = data.get('voice', 'Rachel')
    model = data.get('model', 'eleven_multilingual_v2')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        audio = client.generate(text=text, voice=voice, model=model)
        play(audio)
        return jsonify({"status": "Audio played successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def start_app():
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    start_app()


