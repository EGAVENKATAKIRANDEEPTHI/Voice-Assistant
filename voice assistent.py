import speech_recognition as sr
import pyttsx3
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    recognizer = sr.Recognizer()

    speak("Hello! I am your voice assistant. How can I assist you today?")

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio).lower()
            print("User:", query)

            if "sleep" in query or "exit" in query or "quit" in query:
                speak("Goodbye!")
                break
            elif "open" in query:
                if "google" in query:
                    webbrowser.open("https://www.google.com")
                elif "youtube" in query:
                    webbrowser.open("https://www.youtube.com")
                elif "instagram" in query:
                    webbrowser.open("https://www.instagram.com")
                elif "facebook" in query:
                    webbrowser.open("https://www.facebook.com")
                elif "spotify" in query:
                    webbrowser.open("https://www.spotify.com")
                elif "github" in query:
                    webbrowser.open("https://www.github.com")
                elif "mail" in query or "email" in query:
                    webbrowser.open("https://www.gmail.com")
                else:
                    webbrowser.open("https://www.google.com/search?q=" + query.replace("open ", ""))
                speak(f"Opening {query.replace('open ', '')}.")
            else:
                speak("Sorry, I didn't understand. Can you repeat?")
        except Exception as e:
            print(e)
            speak("Sorry, I couldn't process your request. Can you repeat?")

if __name__ == "__main__":
    main()
