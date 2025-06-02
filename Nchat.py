import random

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
            "Experimenting with IoT devices might spark new interests."
        ]
        self.fallback_responses = [
            "Sorry, I didn't quite catch that. Can you rephrase?",
            "I'm not sure about that. Can you ask something else?",
            "That's interesting! Tell me more or ask a different question."
        ]

    def greet(self):
        print(random.choice(self.greetings))

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Simple keyword matching for responses
        if any(q in user_input for q in ["how are you", "how's it going"]):
            return "I'm a bot, so I don't have feelings, but I'm here to help you!"
        elif any(q in user_input for q in ["your name", "who are you"]):
            return "I'm a friendly Python chatbot created to assist you."
        elif any(q in user_input for q in ["what can you do", "help", "features"]):
            return "I can greet you, answer simple questions, and suggest new ideas!"
        elif any(q in user_input for q in ["thank you", "thanks"]):
            return "You're welcome! If you have more questions, just ask."
        elif any(q in user_input for q in ["suggest", "idea", "something new"]):
            return self.suggest_idea()
        elif "exit" in user_input or "quit" in user_input:
            return "exit"
        else:
            return random.choice(self.fallback_responses)

    def suggest_idea(self):
        return random.choice(self.ideas)

def main():
    bot = SimpleChatBot()
    bot.greet()
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        response = bot.get_response(user_input)
        if response == "exit":
            print("ChatBot: Goodbye! Have a great day!")
            break
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
