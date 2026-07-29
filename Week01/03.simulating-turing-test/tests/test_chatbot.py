import pytest
from src.chatbot import SimpleChatbot


@pytest.fixture
def chatbot():
    return SimpleChatbot()


def test_greeting(chatbot):
    response = chatbot.get_response("hello")
    assert "Hello there!" in response

    response = chatbot.get_response("HI there")
    assert "Hello there!" in response


def test_fallback(chatbot):
    response = chatbot.get_response("some random text")
    assert response == chatbot.fallback_response


def test_exit_keywords(chatbot):
    assert chatbot.get_response("bye") == "Goodbye!"
    assert chatbot.get_response("EXIT ") == "Goodbye!"
    assert chatbot.get_response("quit") == "Goodbye!"


def test_case_insensitivity(chatbot):
    response = chatbot.get_response("How Are You")
    assert "I'm just a computer program" in response
