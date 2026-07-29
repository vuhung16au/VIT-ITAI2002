import sys
import os
import unittest
import io

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import run_simulation

class TestMain(unittest.TestCase):
    def test_run_simulation(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        run_simulation(steps=2, initial_dirty_positions=[0, 1])
        
        sys.stdout = sys.__stdout__
        self.assertIn("Simulation Ended", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
