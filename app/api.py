
from flask import Flask, request, jsonify
import soundfile as sf

from .noise_filter import reduce_noise
from .speech_detector import detect_speech
from .config import SAMPLE_RATE

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/detect', methods=['POST'])
def detect():
    if 'audio' not in request.files:
        return jsonify({"error": "audio file required"}), 400

    file = request.files['audio']
    audio, sr = sf.read(file)

    if sr != SAMPLE_RATE:
        return jsonify({"error": "audio must be 16kHz"}), 400

    cleaned = reduce_noise(audio, sr)
    result = detect_speech(cleaned * 32767)

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
