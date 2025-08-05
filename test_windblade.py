# test_windblade.py
"""
Tests for WindBlade module.
"""

import unittest
from windblade import WindBlade

class TestWindBlade(unittest.TestCase):
    """Test cases for WindBlade class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WindBlade()
        self.assertIsInstance(instance, WindBlade)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WindBlade()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
