# Quickstart

Follow these steps to set up and run the Agent-Environment Interaction project.

## Prerequisites
- Python 3.9+
- `make`
- `uv` (install via `curl -LsSf https://astral.sh/uv/install.sh | sh`)

## Setup

1. **Create and activate a virtual environment with uv:**
   ```bash
   uv venv
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```

## Running the Project

To run the demonstration (which executes `src/main.py`):
```bash
make demo
```

To run the test suite (which executes `pytest`):
```bash
make test
```

## Linting and Formatting
To format the code with `black`:
```bash
make format
```

To lint the code with `ruff`:
```bash
make lint
```
