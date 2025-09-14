# Python Voice Assistant

This is a modular voice assistant built in Python. It listens for voice commands, responds with speech, and performs basic tasks like greeting, speaking text aloud, and exiting gracefully. It’s designed to be easy to expand—whether you want to add PDF reading, Wikipedia search, or even ChatGPT integration.

---

## Features

- Voice activation with the phrase: **"Hello Python"**
- Graceful shutdown via: **"exit"**, **"stop"**, or **"quit"**
- Text-to-speech using gTTS
- Modular structure for easy updates
- Color-coded terminal output and progress bars for feedback

---

## Setup Instructions

### 1. Create a virtual environment

Open PowerShell in your project folder and run:

```powershell
python -m venv venv
```

### 2. Activate the environment 

.\venv\Scripts\Activate.ps1

If you get a permission error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
then activate again

### 3. Install dependencies

pip install wikipedia colorama SpeechRecognition pyttsx3 pypiwin32 rich python-docx PyMuPDF gtts playsound

If you're using Python 3.13, install PyAudio manually:

pip install "C:/Users/monika Bhati/Downloads/PyAudio-0.2.14-cp313-cp313-win_amd64.whl"

### Running the Assistant
Make sure you're in the root folder and your virtual environment is active. Then run:

python .\Voice-Assistant-master\Project_Basic_struct\VoiceAssistant_main.py

### How to Use

Once running, speak clearly into your microphone:
- Say "Hello Python" to activate
- Say "Text to speech" to speak custom text
- Say "Exit" or "Stop" to shut it down
If speech isn’t recognized, it will prompt you to try again.

### Notes
- Your microphone must be enabled and accessible
- If you have multiple mics, use list_mics.py to find the correct device index
- You can expand this project with new commands, file reading, or even a GU
