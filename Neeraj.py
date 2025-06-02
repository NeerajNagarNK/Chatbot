import random
import speech_recognition as sr
import pyttsx3

class SimpleChatBot:
    def __init__(self):
        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Feel free to ask me anything.",
            "Greetings! What would you like to know?"
        ]
        self.ideas = [
            "Have you considered learning a new programming language?",
            "How about starting a blog to share your knowledge?",
            "Creating a personal website can be a great idea!",
            "Why not explore machine learning or AI projects?",
            "You could develop a mobile app to solve a daily problem.",
            "Try building a game or interactive story.",
            "Contributing to open source projects can be very rewarding.",
            "Experimenting with IoT devices might spark new interests.",
            " Try Online work",
            "Learn Stock Market",
            "Learn new Technology Trends like AR,VR",
            " Learn Computer Networks",
            " you go to treditional practic like Enginear, Doctor, Loyer",
            " Learn any sports like Socar, cricket, Hockey, Swiming or any other sport"
        ]
        self.fallback_responses = [
            "Sorry, I didn't quite catch that. Can you rephrase?",
            "I'm not sure about that. Can you ask something else?",
            "That's interesting! Tell me more or ask a different question.",
            " kya aap Hindi me puchna chahenge, ya aapko english aati hai"
        ]

    def greet(self):
        return random.choice(self.greetings)

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Simple keyword matching for responses
        if any(q in user_input for q in ["how are you", "how's it going"]):
            return "I'm a neeraj, if yo want any help I'm here to help you!"
        elif any(q in user_input for q in ["your name", "who are you"]):
            return "I'm neeraj, you need any help please tell me, assist you."
        elif any(q in user_input for q in ["what can you do", "help", "features"]):
            return "I can greet you, answer your questions, and suggest new ideas!"
        elif any(q in user_input for q in ["thank you", "thanks"]):
            return "You're welcome! If you have more questions, just ask."
        elif any(q in user_input for q in ["suggest", "idea", "something new"]):
            return self.suggest_idea()
        elif any(q in user_input for q in [" Joke", "Comedy"]):
            return " I am not a Joker please don't west my time and your Money"
        elif "exit" in user_input or "quit" in user_input:
            return "exit"
        else:
            return random.choice(self.fallback_responses)

    def suggest_idea(self):
        return random.choice(self.ideas)

def speak_text(text, engine):
    engine.say(text)
    engine.runAndWait()

def listen_and_recognize(recognizer, microphone):
    with microphone as source:
        print("Listening... (say something or say 'exit' to quit)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the speech recognition service.")
        return ""

def main():
    bot = SimpleChatBot()
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Optionally change voice here if multiple are available
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)

    print("=== Voice-enabled ChatBot ===")
    greeting = bot.greet()
    print("ChatBot:", greeting)
    speak_text(greeting, engine)

    # Try to get a microphone device
    try:
        mic = sr.Microphone()
    except OSError:
        print("No microphone detected, switching to text input.")
        mic = None

    while True:
        if mic:
            user_input = listen_and_recognize(recognizer, mic)
            if not user_input:
                # Fallback to text input if recognition fails
                user_input = input("You (type): ").strip()
        else:
            user_input = input("You: ").strip()

        if not user_input:
            continue

        response = bot.get_response(user_input)
        if response == "exit":
            print("ChatBot: Goodbye! Have a great day!")
            speak_text("Goodbye! Have a great day!", engine)
            break

        print("ChatBot:", response)
        speak_text(response, engine)

if __name__ == "__main__":
    main()
