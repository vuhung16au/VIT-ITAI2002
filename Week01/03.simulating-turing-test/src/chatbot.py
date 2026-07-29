import re
from typing import Dict


class SimpleChatbot:
    """A simple conversational agent simulating the Turing Test.

    It uses a dictionary of predefined patterns and responses.
    """

    def __init__(self) -> None:
        # Dictionary of predefined patterns and corresponding responses
        self.responses: Dict[str, str] = {
            r"\b(hello|hi|hey)\b": "Hello there! How can I help you today?",
            r"\bhow are you\b": (
                "I'm just a computer program, but I'm doing well! How about you?"
            ),
            r"\b(what is your name|who are you)\b": (
                "I am a simple chatbot created to simulate the Turing Test."
            ),
            r"\bweather\b": (
                "I cannot check the weather, but I hope it's nice where you are!"
            ),
            r"\bjoke\b": (
                "Why do programmers prefer dark mode? Because light attracts bugs!"
            ),
            r"\b(thanks|thank you)\b": "You're welcome!",
        }
        self.fallback_response = "I don't understand that."
        self.exit_keywords = {"bye", "exit", "quit"}

    def get_response(self, user_input: str) -> str:
        """Get an appropriate response based on the user's input.

        Args:
            user_input: The string input provided by the user.

        Returns:
            The chatbot's response string.
        """
        user_input_lower = user_input.lower().strip()

        # Check for exact matches for exit
        if user_input_lower in self.exit_keywords:
            return "Goodbye!"

        # Check for keyword matches
        for pattern, response in self.responses.items():
            if re.search(pattern, user_input_lower):
                return response

        return self.fallback_response

    def start(self) -> None:
        """Start the interactive terminal session."""
        print("Chatbot: Hello! Type 'bye', 'exit', or 'quit' to end the conversation.")
        while True:
            try:
                user_input = input("You: ")
                if not user_input.strip():
                    continue

                response = self.get_response(user_input)
                print(f"Chatbot: {response}")

                if user_input.lower().strip() in self.exit_keywords:
                    break
            except (KeyboardInterrupt, EOFError):
                print("\nChatbot: Goodbye!")
                break


if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.start()
