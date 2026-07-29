import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agent import HomeCleaningRobot
from environment import Environment

class TestAgent(unittest.TestCase):
    def test_agent_initialization(self):
        robot = HomeCleaningRobot(start_position=2)
        self.assertEqual(robot.position, 2)
        self.assertEqual(robot.cleaned_positions, [])

    def test_perceive(self):
        robot = HomeCleaningRobot()
        env = Environment([0, 1])
        self.assertTrue(robot.perceive(env))
        
        env = Environment([1, 2])
        self.assertFalse(robot.perceive(env))

    def test_decide(self):
        robot = HomeCleaningRobot()
        self.assertEqual(robot.decide(True), "Clean")
        self.assertEqual(robot.decide(False), "Move Forward")

    def test_act_clean(self):
        robot = HomeCleaningRobot(start_position=0)
        env = Environment([0])
        robot.act("Clean", env)
        self.assertFalse(env.is_dirty(0))
        self.assertEqual(robot.cleaned_positions, [0])
        self.assertEqual(robot.position, 0)

    def test_act_move(self):
        robot = HomeCleaningRobot(start_position=0)
        env = Environment([])
        robot.act("Move Forward", env)
        self.assertEqual(robot.position, 1)
        self.assertEqual(robot.cleaned_positions, [])

if __name__ == '__main__':
    unittest.main()
