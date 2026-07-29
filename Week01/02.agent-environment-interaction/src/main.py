from src.environment import GridEnvironment
from src.agent import RationalAgent

def run_simulation():
    """
    Sets up the environment and runs the simulation loop.
    """
    size = 5
    goal_pos = (4, 4)
    obstacles = [(1, 1), (1, 2), (1, 3), (3, 1), (3, 2), (2, 4)]
    
    env = GridEnvironment(size=size, obstacles=obstacles, goal=goal_pos)
    agent = RationalAgent(start_pos=(0, 0))

    print(f"Initial Grid:\n{env.grid}")
    print(f"Agent starting at: {(agent.r, agent.c)}")
    print(f"Goal is at: {goal_pos}")

    step = 0
    max_steps = 50 # Safeguard against infinite loops

    while step < max_steps:
        if agent.perceive(env):
            print(f"Step {step}: Agent reached the goal at {(agent.r, agent.c)}!")
            break
            
        print(f"Step {step}: Agent is at {(agent.r, agent.c)}")
        agent.decide(env, goal_pos)
        step += 1

    if step >= max_steps:
        print("Agent failed to reach the goal within the maximum number of steps.")
        print(f"Agent history: {agent.history}")
    else:
        print(f"Success! Agent history: {agent.history}")

if __name__ == "__main__":
    run_simulation()
