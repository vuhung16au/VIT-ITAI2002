# Activity PRD: Building a Simple Intelligent Agent

## Objective
To build a basic, rule-based intelligent agent in Python (a `HomeCleaningRobot`) that can perceive its environment and act accordingly based on a set of rules. This introduces students to the fundamental concepts of sensors, decision-making, and actuators in code.

## Requirements
1. Define a Python class `HomeCleaningRobot`.
2. The robot must have a state to track its position (`self.position`).
3. Implement a `perceive` method that takes an environment state as input and returns whether the current position is "dirty".
4. Implement a `decide` method that takes the perception as input. It should return `"Clean"` if dirty, and `"Move Forward"` if clean.
5. Implement an `act` method that executes the decision (updates a `cleaned_positions` list or advances `self.position`).
6. Create an `Environment` class that holds dirty positions.
7. Run a simulation loop for `N` steps, calling `perceive`, `decide`, and `act` sequentially.

## Acceptance Criteria
- The Python code runs without errors.
- The simulation loop correctly identifies dirty spots and cleans them, outputting standard print statements for each action.
- The code uses core Python types (classes, lists) appropriately without relying on complex external libraries.

## Folder structure

- README.md
- PRD.md (this file)
- Makefile
- QUICKSTART.md
- src/
  - main.py
  - agent.py
  - environment.py
  - test/
    - test_agent.py
    - test_environment.py
    - test_main.py
- `docs/*.md` (optional documentation files): please include any additional documentation files in the `docs` folder if necessary.

## `Makefile` 

include target `make demo`: This will demo our project