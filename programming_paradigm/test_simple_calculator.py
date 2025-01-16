import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Positive numbers
        self.assertEqual(self.calc.add(-1, -1), -2)  # Negative numbers
        self.assertEqual(self.calc.add(0, 5), 5)  # Zero and positive
        self.assertEqual(self.calc.add(-5, 5), 0)  # Negative and positive
        self.assertEqual(self.calc.add(1.5, 2.3), 3.8)  # Floats

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Positive numbers
        self.assertEqual(self.calc.subtract(0, 5), -5)  # Zero and positive
        self.assertEqual(self.calc.subtract(-5, -5), 0)  # Negative numbers
        self.assertEqual(self.calc.subtract(10, -5), 15)  # Positive and negative
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)  # Floats

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)  # Positive numbers
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Zero and positive
        self.assertEqual(self.calc.multiply(-3, 3), -9)  # Negative and positive
        self.assertEqual(self.calc.multiply(-3, -3), 9)  # Negative numbers
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)  # Floats

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)  # Positive numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)  # Negative and positive
        self.assertEqual(self.calc.divide(-10, -2), 5)  # Negative numbers
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5, places=1)  # Floats with precision

if __name__ == "__main__":
    unittest.main()

