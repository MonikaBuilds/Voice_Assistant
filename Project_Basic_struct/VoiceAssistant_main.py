from speakListen import short_hear, greet, speak
from TextTospeech import text_to_speech
from colorama import Fore

def main():
    greet("start")

    while True:
        query = short_hear().lower()

        if query == "none":
            print(Fore.RED + "Could not recognize speech. Try again or say 'exit' to quit.")
            continue

        if "exit" in query or "stop" in query or "quit" in query:
            greet("quit")
            break

        if "hello python" in query:
            greet("start")

        elif "text to speech" in query:
            speak("Please say the text you want me to speak.")
            text = short_hear()
            if text != "none":
                text_to_speech(text)

        else:
            speak("I didn't catch that. Please say 'Hello Python' or 'Exit'.")

if __name__ == "__main__":
    main()