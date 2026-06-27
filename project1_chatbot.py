"""
Project 1: Rule-Based AI Chatbot
DecodeLabs Industrial Training Kit - AI Track

Goal: A simple rule-based chatbot that responds to predefined user inputs
using if-else / dictionary logic, runs in a continuous loop, and exits
cleanly on command.
"""


responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bunch of code, but I'm running great!",
    "what is your name": "I'm ChatBot, your friendly rule-based assistant.",
    "what can you do": "I can chat with you using simple predefined rules.",
    "help": "Try greeting me, asking my name, or typing 'bye' to exit.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
}

EXIT_COMMANDS = {"bye", "exit", "quit"}


def sanitize_input(raw_input: str) -> str:
    """Phase 1: Sanitization & Normalization."""
    return raw_input.lower().strip()


def get_response(user_input: str) -> str:
    """Phase 2: Process - Intent Matching using dictionary .get()."""
    return responses.get(user_input, "I do not understand. Type 'help' for options.")


def run_chatbot():
    print("=" * 50)
    print(" Welcome to DecodeLabs Rule-Based Chatbot")
    print(" Type 'bye', 'exit', or 'quit' to end the chat.")
    print("=" * 50)


    while True:
        raw_input_text = input("\nYou: ")
        clean_input = sanitize_input(raw_input_text)

     
        if clean_input in EXIT_COMMANDS:
            print("Bot: Goodbye! Have a great day.")
            break

        reply = get_response(clean_input)
        print(f"Bot: {reply}")


if __name__ == "__main__":
    run_chatbot()
