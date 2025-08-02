# test_elitespectral.py
"""
Tests for EliteSpectral module.
"""

import unittest
from elitespectral import EliteSpectral

class TestEliteSpectral(unittest.TestCase):
    """Test cases for EliteSpectral class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EliteSpectral()
        self.assertIsInstance(instance, EliteSpectral)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EliteSpectral()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
