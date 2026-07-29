import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from environment import Environment
from agent import HomeCleaningRobot

def run_simulation(steps, initial_dirty_positions):
    environment = Environment(initial_dirty_positions)
    robot = HomeCleaningRobot()

    print(f"Starting simulation for {steps} steps.")
    print(f"Initial dirty positions: {initial_dirty_positions}")

    for step in range(steps):
        print(f"\n--- Step {step + 1} ---")
        perception = robot.perceive(environment)
        decision = robot.decide(perception)
        robot.act(decision, environment)

    print("\n--- Simulation Ended ---")
    print(f"Robot final position: {robot.position}")
    print(f"Cleaned positions: {robot.cleaned_positions}")
    print(f"Remaining dirty spots in environment: {list(environment.dirty_positions)}")

if __name__ == "__main__":
    initial_dirty_spots = [0, 2, 3, 5]
    run_simulation(steps=7, initial_dirty_positions=initial_dirty_spots)
