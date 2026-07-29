import pytest
from src.environment import GridEnvironment
from src.agent import RationalAgent

def test_environment_initialization():
    env = GridEnvironment(size=5, obstacles=[(1, 1)], goal=(4, 4))
    
    assert env.size == 5
    assert env.grid.shape == (5, 5)
    assert env.grid[1, 1] == 1 # Obstacle
    assert env.grid[4, 4] == 2 # Goal
    assert env.grid[0, 0] == 0 # Empty

def test_environment_bounds():
    env = GridEnvironment(size=5, obstacles=[], goal=(4, 4))
    
    assert env.is_valid_position(0, 0) == True
    assert env.is_valid_position(4, 4) == True
    assert env.is_valid_position(5, 5) == False
    assert env.is_valid_position(-1, 0) == False

def test_agent_perceive():
    env = GridEnvironment(size=5, obstacles=[], goal=(4, 4))
    agent = RationalAgent(start_pos=(4, 4))
    
    assert agent.perceive(env) == True
    
    agent2 = RationalAgent(start_pos=(0, 0))
    assert agent2.perceive(env) == False

def test_agent_decide_no_obstacles():
    env = GridEnvironment(size=5, obstacles=[], goal=(4, 4))
    agent = RationalAgent(start_pos=(0, 0))
    
    agent.decide(env, (4, 4))
    # Should move down or right
    assert agent.r + agent.c == 1
    assert (agent.r, agent.c) in [(1, 0), (0, 1)]

def test_agent_decide_obstacle_avoidance():
    # Block immediate right and down
    env = GridEnvironment(size=5, obstacles=[(0, 1), (1, 0)], goal=(4, 4))
    agent = RationalAgent(start_pos=(0, 0))
    
    # Normally wants to go right or down, but both are blocked. 
    # Since only (0,0) is valid and no other move, it might be trapped, or stay.
    # Actually, it can't move to (-1,0) or (0,-1).
    agent.decide(env, (4, 4))
    assert agent.r == 0 and agent.c == 0 # Trapped

def test_agent_reaches_goal():
    env = GridEnvironment(size=3, obstacles=[(0, 1), (1, 1)], goal=(2, 2))
    agent = RationalAgent(start_pos=(0, 0))
    
    # Let it run for a few steps
    for _ in range(10):
        if agent.perceive(env):
            break
        agent.decide(env, (2, 2))
        
    assert agent.perceive(env) == True
    assert (agent.r, agent.c) == (2, 2)
