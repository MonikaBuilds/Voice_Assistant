from gtts import gTTS
from playsound import playsound
import os

def text_to_speech(text, filename="output.mp3"):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"Error in text_to_speech: {e}")