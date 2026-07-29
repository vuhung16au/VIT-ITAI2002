.PHONY: demo test format lint

PYTHON = uv run python
PYTEST = uv run pytest
BLACK = uv run black
FLAKE8 = uv run flake8

demo:
	$(PYTHON) -m src.chatbot

test:
	PYTHONPATH=. $(PYTEST) tests/

format:
	$(BLACK) src/ tests/

lint:
	$(FLAKE8) --max-line-length 88 src/ tests/
