"""
CODSOFT AI Internship - Task 1
Rule-Based Chatbot
"""

def get_response(user_input):
    text = user_input.lower().strip()

    if any(word in text for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! It was nice talking with you."

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! How can I help you?"

    if "your name" in text or "who are you" in text:
        return "I'm a simple rule-based AI chatbot. How can I help you?"

    if text.startswith("my name is "):
        name = user_input.strip()[11:].strip()
        if name:
            return f"Nice to meet you, {name}!"

    if "help" in text or "what can you do" in text:
        return "I can respond to greetings, answer common questions, tell you about AI, and have a simple conversation."

    if "artificial intelligence" in text or text == "ai" or "what is ai" in text:
        return "Artificial Intelligence (AI) is the field of creating systems that can perform tasks that normally require human intelligence."

    if "internship" in text:
        return "This is a simple rule-based chatbot project created as part of an AI internship task."

    if "how are you" in text:
        return "I'm doing great! Thanks for asking."

    if "thank" in text:
        return "You're welcome! Happy to help."

    return "Sorry, I don't understand that yet. Please try a common question such as 'Hello', 'What is your name?', 'What can you do?', or 'What is AI?'."


def main():
    print("=" * 55)
    print("             RULE-BASED AI CHATBOT")
    print("=" * 55)
    print("Type 'bye', 'exit', or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something so I can respond.")
            continue

        response = get_response(user_input)
        print("Bot:", response)

        if any(word in user_input.lower().strip() for word in ["bye", "goodbye", "exit", "quit"]):
            break


if __name__ == "__main__":
    main()
