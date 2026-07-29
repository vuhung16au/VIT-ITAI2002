# Activity PRD: Agent-Environment Interaction (Grid World)

## Objective
To simulate a 2D environment using `numpy` and design an agent capable of rationally navigating this grid to reach a specific goal coordinate, while avoiding basic obstacles. This reinforces the concept of Rationality and Introduces NumPy.

## Requirements
1. Import and utilize the `numpy` library.
2. Define a `GridEnvironment` class that initializes a 2D `numpy` array of size `N x N`. 
3. Use integers to represent different states in the `numpy` grid (e.g., `0` for empty, `1` for obstacle, `2` for goal).
4. Define a `RationalAgent` class that starts at coordinate `(0,0)`.
5. The agent must have a `perceive` method that checks its current coordinate against the environment bounds and obstacles.
6. The agent must have a `decide` method that prefers moving toward the goal coordinates if the path is not an obstacle. If the preferred path is blocked, it should make an alternative safe move.
7. The agent must terminate the simulation loop when the goal coordinate is reached.

## Acceptance Criteria
- The code successfully uses `numpy` to represent the environment state space.
- The `RationalAgent` successfully navigates from `(0,0)` to the goal without hitting obstacles.
- The output displays the step-by-step coordinates of the agent as it navigates the grid.
- Proper boundary checking is implemented so the agent does not move off the grid.



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