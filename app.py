import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""   # Force CPU

import torch
torch.set_num_threads(1)

from flask import Flask, render_template, request, jsonify
from TTS.api import TTS
import uuid, subprocess

app = Flask(__name__)

AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# --------- LAZY LOAD TTS (CRITICAL FIX) ---------
tts = None

def get_tts():
    global tts
    if tts is None:
        tts = TTS(
            model_name="tts_models/en/ljspeech/tacotron2-DDC",
            gpu=False,
            progress_bar=False
        )
    return tts
# -----------------------------------------------

TONE_PRESETS = {
    "neutral": 1.0,
    "calm": 1.2,
    "energetic": 0.85,
    "professional": 0.95
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    text = data.get("text", "").strip()
    speed = float(data.get("speed", 1.0))
    tone = data.get("tone", "neutral")
    pitch = float(data.get("pitch", 1.0))

    if not text:
        return jsonify({"error": "Text required"}), 400

    length_scale = TONE_PRESETS.get(tone, 1.0) * speed

    wav_name = f"{uuid.uuid4()}.wav"
    pitched_wav = f"p_{wav_name}"
    mp3_name = wav_name.replace(".wav", ".mp3")

    wav_path = os.path.join(AUDIO_DIR, wav_name)
    pitched_path = os.path.join(AUDIO_DIR, pitched_wav)
    mp3_path = os.path.join(AUDIO_DIR, mp3_name)

    # 🔥 Load model ONLY when needed
    tts_engine = get_tts()

    # Generate speech
    tts_engine.tts_to_file(
        text=text,
        file_path=wav_path,
        length_scale=length_scale
    )

    # Pitch control (FFmpeg)
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", wav_path,
            "-filter:a", f"asetrate=44100*{pitch},atempo={1/pitch}",
            pitched_path
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Convert to MP3
    subprocess.run(
        ["ffmpeg", "-y", "-i", pitched_path, mp3_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    os.remove(wav_path)
    os.remove(pitched_path)

    return jsonify({
        "success": True,
        "audio_url": f"/static/audio/{mp3_name}"
    })

if __name__ == "__main__":
    app.run()
