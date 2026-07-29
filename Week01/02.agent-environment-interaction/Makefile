.PHONY: demo test format lint clean

# Default python command, can be overridden
PYTHON ?= uv run python
PYTEST ?= uv run pytest

demo:
	PYTHONPATH=. $(PYTHON) src/main.py

test:
	PYTHONPATH=. $(PYTEST) src/test/

format:
	uv run black src/

lint:
	uv run ruff check src/

clean:
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf src/test/__pycache__
	rm -rf .pytest_cache
