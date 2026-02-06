```markdown
<div align="center">

# 🎙️ AI Custom Voice Assistant  
### Neural Text-to-Speech with Speed, Tone & Pitch Control

A **production-ready AI-powered Text-to-Speech web app** that converts text into natural-sounding speech using a **custom AI voice**, with full control over **speed, tone presets, and pitch**.  
Built with **Flask + Coqui TTS** and deployable as a **mobile-friendly PWA**.

---

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![AI](https://img.shields.io/badge/AI-Neural%20TTS-purple)
![FFmpeg](https://img.shields.io/badge/Audio-FFmpeg-green)
![Deployment](https://img.shields.io/badge/Deployed-Railway-success)

</div>

---

## ✨ Features

- 🎧 **Neural Text-to-Speech** using Coqui TTS  
- 🎭 **Tone Presets**: Calm, Neutral, Energetic, Professional  
- ⏩ **Speed Control** via intuitive slider  
- 🎚 **Pitch Control** using FFmpeg audio processing  
- 🔊 Real-time audio playback  
- 💾 MP3 audio generation  
- 📱 Mobile-friendly UI  
- 📦 **Progressive Web App (PWA)** support  
- ☁️ Cloud-deployable (Railway compatible)

---

## 🧠 How It Works

1. User enters text
2. Selects:
   - Speed
   - Pitch
   - Tone preset
3. Backend generates speech using **neural TTS**
4. FFmpeg applies pitch transformation
5. Audio is converted to MP3
6. Output is streamed back to the browser

---

## 🛠️ Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript  
- Progressive Web App (PWA)

### Backend
- Python  
- Flask  
- Gunicorn  
- Coqui TTS (Neural Text-to-Speech)

### Audio Processing
- FFmpeg

### Deployment
- Railway  
- Nixpacks

---

## 📁 Project Structure

```

ai-custom-voice/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── nixpacks.toml
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   └── audio/
│
├── manifest.json
└── service-worker.js

````

---

## ⚙️ Local Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-custom-voice.git
cd ai-custom-voice
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install FFmpeg

* **Linux**: `sudo apt install ffmpeg`
* **macOS**: `brew install ffmpeg`
* **Windows**: Download from [https://ffmpeg.org](https://ffmpeg.org)

### 5️⃣ Run the App

```bash
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

## ☁️ Deployment (Railway)

1. Push code to GitHub
2. Create a new Railway project
3. Connect GitHub repository
4. Railway auto-builds using `nixpacks.toml`
5. FFmpeg installs automatically
6. App goes live 🚀

---

## 📌 Use Cases

* 🎥 YouTube & Reel voiceovers
* 📚 Study & revision assistant
* 🎙 Podcast narration
* ♿ Accessibility (text reading)
* 🧪 AI & speech research demos

---

## 🔮 Future Enhancements

* 🌍 Multi-language voices (Tamil / Hindi)
* 🧬 Voice cloning
* 💾 Audio history
* 🎨 Advanced UI animations
* 🔐 User accounts

---

## 👨‍💻 Author

**Hari Prasath**
AI & Data Science Student
Focused on AI, Conversational Systems & Voice Technologies

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🧠 Share feedback

Your support motivates future improvements 🚀

```
