# Project 1: Rule-Based AI Chatbot 

## Project Overview
A foundational rule-based chatbot that responds to predefined user inputs using dictionary-based lookup and conditional logic. This project introduces core AI concepts through simple programmatic decision-making without machine learning.

## Objectives
- Implement basic control flow and decision-making logic
- Build a chatbot using if-else logic and dictionary lookups
- Create a continuous loop-based interactive application
- Handle user input validation and exit commands

## Project Structure

```
Project1/
├── project1_chatbot.py      # Main chatbot implementation
└── README.md                # This file
```

## Technical Architecture

### Components

1. **Knowledge Base (Dictionary)**
   - O(1) lookup time complexity
   - Contains predefined responses for common inputs
   - Easy to expand with new patterns

2. **Input Sanitization (`sanitize_input`)**
   - Converts input to lowercase
   - Strips whitespace
   - Normalizes user input for matching

3. **Response Generation (`get_response`)**
   - Uses dictionary `.get()` for safe lookups
   - Provides default fallback message if no match found
   - Handles unknown inputs gracefully

4. **Main Loop (`run_chatbot`)**
   - Continuous interaction until exit command
   - Checks for exit commands: "bye", "exit", "quit"
   - Processes input and displays responses

## Features

✓ **Greeting Responses** - Recognizes and responds to greetings (hello, hi)  
✓ **Personal Information** - Provides bot's name and capabilities  
✓ **Help System** - Offers guidance on available commands  
✓ **Exit Handling** - Multiple exit commands recognized  
✓ **User-Friendly Interface** - Clear prompts and formatted output  
✓ **Fallback Mechanism** - Graceful handling of unknown inputs  

## Current Responses Dictionary

```python
{
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bunch of code, but I'm running great!",
    "what is your name": "I'm ChatBot, your friendly rule-based assistant.",
    "what can you do": "I can chat with you using simple predefined rules.",
    "help": "Try greeting me, asking my name, or typing 'bye' to exit.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
}
```

## Requirements

- Python 3.7+
- No external dependencies required
- Standard library only

## Installation & Setup

1. Navigate to Project1 directory:
   ```bash
   cd Project1
   ```

2. Run the chatbot:
   ```bash
   python project1_chatbot.py
   ```

## Usage Example

```
==================================================
 Welcome to DecodeLabs Rule-Based Chatbot 
 Type 'bye', 'exit', or 'quit' to end the chat.
==================================================

You: hello
Bot: Hi there! How can I help you today?

You: what is your name
Bot: I'm ChatBot, your friendly rule-based assistant.

You: thank you
Bot: You're welcome!

You: bye
Bot: Goodbye! Have a great day. 
```

## Code Verification ✓

**Requirements Met:**
- ✓ Uses dictionary-based lookup for O(1) response time
- ✓ Implements if-else logic for exit handling
- ✓ Runs continuous loop until exit command
- ✓ Sanitizes and normalizes user input
- ✓ Provides helpful fallback messages
- ✓ Clean code structure following best practices

## Suggested Enhancements

1. **Expand Vocabulary**
   - Add more greeting variations
   - Include weather, time, or joke features
   - Add contextual responses

2. **Personality Enhancement**
   - Add random variation to responses
   - Include emoji and formatting
   - Create different "modes" for chatbot

3. **Advanced Logic**
   - Implement pattern matching with wildcards
   - Add context memory (remember user name)
   - Create response categories by topic

4. **User Experience**
   - Add command history/recall
   - Implement response suggestions
   - Add conversation logging

## Learning Outcomes

By completing this project, you will understand:
- Basic control flow and loops
- Dictionary data structures for fast lookups
- Input validation and sanitization
- User-friendly console application design
- Exception handling with graceful exits

## Key Concepts Reinforced

- **Dictionary Lookups**: O(1) complexity for quick response retrieval
- **String Normalization**: Consistent input processing
- **Loop Control**: Continuous operation with exit conditions
- **Fallback Mechanisms**: Handling unknown inputs gracefully
- **User Interface Design**: Clear prompts and feedback

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Chatbot not responding | Ensure exact input matches dictionary keys (after lowercasing) |
| Program won't exit | Use "bye", "exit", or "quit" (case-insensitive) |
| No fallback response | Check if input is in responses dictionary |

