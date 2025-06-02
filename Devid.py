import pyttsx3  # Text-to-speech engine
import speech_recognition as sr  # Speech recognition
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')  # Using SAPI5 on Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set voice (0 for male, 1 for female)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    else :
        speak("Good evening")
    speak(" I am Devid May i help you Sir")    

def takecommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 600
        audio = r.listen(source)
     try:
         print(" Recognizing.....")
         query = r.recognize_google(audio,language = 'en-in')
         print(f"User said: {query}\n")
     except Exception as e:
        #  print(e)
         print(" Please Say that Again.....")                   
         return "None"
     return query

if __name__ == "__main__":
    # speak("Raghav nagar is very ppor Boy")
    wishme()
    while True:
        query= takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia", " ")
            result = wikipedia.summary(query, sentences=1)
            speak("I Found the Data ")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.co.in")    
        elif 'open neerajnagarnk' in query:
            webbrowser.open("neerajnagar777/youtube.com")
        elif 'open tradingview' in query:
            webbrowser.open("tradingview.com") 
        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,  the time is { strTime}")
        elif 'story' in query:
            speak("The Lions Share: The lion took all portions of a hunt, leaving none for others.Moral: The   strong often exploit the weak. The Boy Who Cried Wolf: A young boy tending sheep lied about a wolf attacking them. When a real wolf came, no one believed him.Moral: Always tell the truth; otherwise, people wont believe you when it matters.")
       

            