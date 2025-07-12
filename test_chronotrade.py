# test_chronotrade.py
"""
Tests for ChronoTrade module.
"""

import unittest
from chronotrade import ChronoTrade

class TestChronoTrade(unittest.TestCase):
    """Test cases for ChronoTrade class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChronoTrade()
        self.assertIsInstance(instance, ChronoTrade)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChronoTrade()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
