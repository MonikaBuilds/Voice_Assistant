import time
import datetime
import speech_recognition as sr
import pyttsx3
from colorama import Fore
from rich.progress import Progress

# Initialize text-to-speech engine
python = pyttsx3.init("sapi5")
voices = python.getProperty("voices")
python.setProperty("voice", voices[1].id)
python.setProperty("rate", 140)

def speak(text):
    python.say(text)
    python.runAndWait()

def greet(g):
    hour = datetime.datetime.now().hour
    if g in ["start", "s"]:
        if 0 < hour < 12:
            text = "Hello! Good Morning."
        elif 12 <= hour < 17:
            text = "Hello! Good Afternoon."
        else:
            text = "Hello! Good Evening."
        text += " I am Python. How may I help you?"
        speak(text)
    elif g in ["quit", "end", "over", "e"]:
        speak("Thank you. Good bye!")

def recognizing():
    with Progress() as pr:
        task = pr.add_task("[red]Recognizing...", total=100)
        while not pr.finished:
            pr.update(task, advance=1.0)
            time.sleep(0.01)

def hear(duration=9):
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print(Fore.RED + "\nListening...")
        audio = recognizer.record(source, duration=duration)
        try:
            recognizing()
            text = recognizer.recognize_google(audio)
            print(text + "\n")
            return text
        except Exception as e:
            print(e)
            return "None"

def short_hear(duration_time=5):
    r = sr.Recognizer()
    r.pause_threshold = 1
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True

    with sr.Microphone(device_index=1) as source:  # Replace 1 with your actual index
        print(Fore.RED + "\nListening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=duration_time)
            print(Fore.RED + "Recognizing...")
            return r.recognize_google(audio)
        except Exception as e:
            print(e)
            return "None"