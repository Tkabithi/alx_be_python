import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a new SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_with_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_with_mixed_signs(self):
        self.assertEqual(self.calc.add(-5, 10), 5)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 4), 4)

    # --- Subtraction Tests ---
    def test_subtraction_with_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtraction_resulting_in_negative(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)

    # --- Multiplication Tests ---
    def test_multiplication_with_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_multiplication_with_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_multiplication_with_two_negatives(self):
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    # --- Division Tests ---
    def test_division_with_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_with_negative_divisor(self):
        self.assertEqual(self.calc.divide(9, -3), -3)

    def test_division_with_negative_dividend(self):
        self.assertEqual(self.calc.divide(-8, 2), -4)

    def test_division_with_two_negatives(self):
        self.assertEqual(self.calc.divide(-8, -2), 4)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))  # Expecting None

    def test_division_resulting_in_float(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

if __name__ == "__main__":
    unittest.main()

