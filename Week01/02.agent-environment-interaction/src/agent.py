from typing import Tuple
from src.environment import GridEnvironment

class RationalAgent:
    """
    A rational agent that navigates a GridEnvironment towards a goal.
    """
    def __init__(self, start_pos: Tuple[int, int] = (0, 0)):
        """
        Initializes the agent.

        Args:
            start_pos (Tuple[int, int]): The starting coordinate (row, col) of the agent.
        """
        self.r, self.c = start_pos
        self.history = [start_pos]

    def perceive(self, env: GridEnvironment) -> bool:
        """
        Perceives if the current location is the goal.

        Args:
            env (GridEnvironment): The environment.

        Returns:
            bool: True if the current location is the goal, False otherwise.
        """
        return env.is_goal(self.r, self.c)

    def decide(self, env: GridEnvironment, goal_pos: Tuple[int, int]):
        """
        Decides the next move to get closer to the goal while avoiding obstacles.
        Updates the agent's position.

        Args:
            env (GridEnvironment): The environment.
            goal_pos (Tuple[int, int]): The coordinate of the goal.
        """
        goal_r, goal_c = goal_pos

        # Possible moves: up, down, left, right
        # Order preference: try to move towards the goal first
        
        # Calculate ideal deltas
        dr = 1 if goal_r > self.r else (-1 if goal_r < self.r else 0)
        dc = 1 if goal_c > self.c else (-1 if goal_c < self.c else 0)

        moves = []
        if dr != 0:
            moves.append((self.r + dr, self.c))
        if dc != 0:
            moves.append((self.r, self.c + dc))
            
        # Add alternative moves in case primary preferred moves are blocked
        for alt_dr, alt_dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            alt_r, alt_c = self.r + alt_dr, self.c + alt_dc
            if (alt_r, alt_c) not in moves:
                moves.append((alt_r, alt_c))

        for next_r, next_c in moves:
            if env.is_valid_position(next_r, next_c) and not env.is_obstacle(next_r, next_c):
                # We found a valid move, let's take it
                # Ensure we don't just loop back to the immediate previous step endlessly 
                # if we have other options (basic avoid getting stuck).
                if len(self.history) > 1 and (next_r, next_c) == self.history[-2]:
                    # This is where we just came from. Let's see if there is another valid move.
                    # If it's the last option, we take it.
                    if len([m for m in moves if env.is_valid_position(m[0], m[1]) and not env.is_obstacle(m[0], m[1])]) > 1:
                        continue 
                
                self.r, self.c = next_r, next_c
                self.history.append((self.r, self.c))
                return
        
        # If no valid moves (completely trapped), do nothing.
