import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sum_two_ints(self):
        self.assertEqual(self.calculator.add(5, -9), -4)

    def test_sum_two_ints_negative(self):
        self.assertNotEqual(self.calculator.add(4, 5), -4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(4, 0)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
