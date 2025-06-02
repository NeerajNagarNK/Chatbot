import pyttsx3  # Text-to-speech engine
import speech_recognition as sr  # Speech recognition

engine = pyttsx3.init('sapi5')  # Using SAPI5 on Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set voice (0 for male, 1 for female)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    # speak("Hello Neeraj I am Devid , May i Help You")
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
       
    try:
        print("You said:", text)
        text = r.recognize_google(audio, language='en-in')
        print(f"user said:{text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print("Request error; {0}".format(e))
        return ""

def chatbot():
    while True:
        speak("Hello! neeraj How can I help you?")
        text = listen()

        # Process the user's text input (replace this with your chatbot logic)
        if "hello Anna" in text or "hi" in text:
            speak("Hello Neeraj sir, have a nice day!")
            break

        response = "I'm still under development, but I'm learning to respond to your requests. Here's some information that might be helpful:"
        speak(response)

# Run the chatbot
chatbot()


