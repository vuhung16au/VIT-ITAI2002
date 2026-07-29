# Activity PRD: Simulating the Turing Test (Simple Chatbot)

## Objective
To build a basic conversational agent (chatbot) in Python that responds to string inputs. This activity practically explores the concepts behind the Turing Test by showing how difficult it is to manually encode human-like conversational responses.

## Requirements
1. Define a `SimpleChatbot` class.
2. The chatbot must contain a dictionary of predefined patterns/keywords and their corresponding responses.
3. Create an interaction loop using Python's `input()` function to continuously accept user input.
4. Implement a keyword-matching or exact-match system to return appropriate responses from the dictionary based on the user's input.
5. Provide a fallback response (e.g., "I don't understand that.") if the user input matches no known keywords.
6. Include a termination keyword (e.g., "bye", "exit") that breaks the interaction loop.

## Acceptance Criteria
- The Python script runs an interactive terminal session where a user can type text.
- The chatbot correctly identifies mapped keywords regardless of case sensitivity (e.g., "HELLO" and "hello" both yield a greeting).
- The fallback response correctly triggers for unknown inputs.
- The interactive loop terminates cleanly when the exit keyword is provided.



## Folder structure

- README.md
- PRD.md (this file)
- Makefile
- QUICKSTART.md
- src/
  - xxx.py
  - test/
    - xxx.py
- `docs/*.md` (optional documentation files): please include any additional documentation files in the `docs` folder if necessary.

## `Makefile` 

include target `make demo`: This will demo our project