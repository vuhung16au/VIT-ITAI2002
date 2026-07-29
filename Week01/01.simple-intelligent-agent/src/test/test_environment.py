import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from environment import Environment

class TestEnvironment(unittest.TestCase):
    def test_environment_initialization(self):
        env = Environment([1, 2, 3])
        self.assertEqual(env.dirty_positions, {1, 2, 3})

    def test_is_dirty(self):
        env = Environment([1, 2, 3])
        self.assertTrue(env.is_dirty(2))
        self.assertFalse(env.is_dirty(4))

    def test_clean(self):
        env = Environment([1, 2, 3])
        env.clean(2)
        self.assertFalse(env.is_dirty(2))
        self.assertEqual(env.dirty_positions, {1, 3})

if __name__ == '__main__':
    unittest.main()
