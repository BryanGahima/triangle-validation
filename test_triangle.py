# test_triangle.py

import unittest
from triangle import is_valid_triangle  # Import the function from triangle.py

class TestTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        """Test that valid triangles return True."""
        self.assertTrue(is_valid_triangle(3, 4, 5))  # 3-4-5 triangle
        self.assertTrue(is_valid_triangle(5, 6, 7))  # Another valid triangle

    def test_invalid_triangle(self):
        """Test that invalid triangles return False."""
        self.assertFalse(is_valid_triangle(1, 2, 3))  # 1+2 is not greater than 3
        self.assertFalse(is_valid_triangle(10, 1, 1))  # 1+1 is not greater than 10

    def test_edge_case(self):
        """Test edge cases where two sides sum to exactly the third side."""
        self.assertFalse(is_valid_triangle(1, 1, 2))  # 1+1 equals 2, not greater

    def test_zero_and_negative(self):
        """Test cases with zero or negative values."""
        self.assertFalse(is_valid_triangle(0, 1, 1))  # 0 cannot be a side
        self.assertFalse(is_valid_triangle(-1, 2, 3))  # Negative side lengths are invalid
