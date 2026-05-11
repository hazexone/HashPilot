# test_hashpilot.py
"""
Tests for HashPilot module.
"""

import unittest
from hashpilot import HashPilot

class TestHashPilot(unittest.TestCase):
    """Test cases for HashPilot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HashPilot()
        self.assertIsInstance(instance, HashPilot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HashPilot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
