import numpy as np
from typing import Tuple, List

class GridEnvironment:
    """
    Represents a 2D grid world environment for an agent to navigate.

    The grid uses the following state representations:
        0: Empty space
        1: Obstacle
        2: Goal
    """
    def __init__(self, size: int, obstacles: List[Tuple[int, int]], goal: Tuple[int, int]):
        """
        Initializes the grid environment.

        Args:
            size (int): The size of the N x N grid.
            obstacles (List[Tuple[int, int]]): A list of (row, col) coordinates for obstacles.
            goal (Tuple[int, int]): The (row, col) coordinate for the goal.
        """
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        
        # Place obstacles
        for r, c in obstacles:
            if 0 <= r < size and 0 <= c < size:
                self.grid[r, c] = 1
                
        # Place goal
        g_r, g_c = goal
        if 0 <= g_r < size and 0 <= g_c < size:
            self.grid[g_r, g_c] = 2

    def is_valid_position(self, r: int, c: int) -> bool:
        """Checks if a position is within the grid boundaries."""
        return 0 <= r < self.size and 0 <= c < self.size

    def is_obstacle(self, r: int, c: int) -> bool:
        """Checks if a position is an obstacle."""
        if not self.is_valid_position(r, c):
            return True # Treat out of bounds as an obstacle
        return self.grid[r, c] == 1

    def is_goal(self, r: int, c: int) -> bool:
        """Checks if a position is the goal."""
        if not self.is_valid_position(r, c):
            return False
        return self.grid[r, c] == 2
