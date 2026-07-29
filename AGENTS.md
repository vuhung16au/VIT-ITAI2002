# Project Guidelines

## Project Structure & Requirements
- Each project must have a `README.md` file providing an overview of the project.
- Each project must have a `QUICKSTART.md` file detailing how to quickly set up and run the project.
- Each project must have a `Makefile` to simplify common command executions.

## Makefile Targets
The `Makefile` must include at least the following targets:
- `make demo`: To run a demonstration of the project.
- `make test`: To run the test suite.

## Testing
- Each project must have unit tests.
- We use **pytest** as our standard testing framework.

## Python Coding Practices
To maintain high code quality, please adhere to the following Python best practices:
1. **Formatting & Linting**: Use `black` for code formatting and `flake8` or `ruff` for linting.
2. **Type Hinting**: Use type hints (`typing` module) for function arguments and return values to improve readability and catch potential bugs early.
3. **Dependency & Package Management**: We prefer using `uv` for package management, resolving dependencies, and building/running Python scripts. Avoid installing packages globally.
4. **Virtual Environments**: Use `uv` to manage virtual environments and isolate project dependencies efficiently.
5. **Documentation**: Write clear docstrings for classes, functions, and modules (e.g., using Google or NumPy style).
6. **Error Handling**: Use specific exception types instead of generic `except Exception:` blocks.
7. **Modularity**: Keep functions focused on a single task (Single Responsibility Principle) and organize code into logical modules and packages.
