import re
import random

# Define intents and responses
intents = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "exit"],
        "responses": ["Goodbye!", "See you later!", "Have a nice day!"]
    },
    "thanks": {
        "keywords": ["thanks", "thank you"],
        "responses": ["You're welcome!", "No problem!", "Happy to help!"]
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "responses": ["I'm a simple NLP chatbot.", "You can call me ChatBot."]
    }
}

def clean_text(text):
    """Lowercase and remove punctuation"""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

def get_intent(user_input):
    """Find matching intent based on keywords"""
    for intent, data in intents.items():
        for keyword in data["keywords"]:
            if keyword in user_input:
                return intent
    return None

def chatbot_response(user_input):
    user_input = clean_text(user_input)
    intent = get_intent(user_input)

    if intent:
        return random.choice(intents[intent]["responses"])
    else:
        return "Sorry, I didn't understand that."

def chat():
    print("Chatbot: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if "exit" in user_input.lower():
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))

if __name__ == "__main__":
    chat()
