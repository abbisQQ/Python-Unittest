import unittest
import calc

"""
In the methods below we test for numeric input and string input
plus in the divide method we also test for zero division error.
"""


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(5, 2), 7)
        self.assertRaises(TypeError, calc.add, "12", "22")

    def test_minus(self):
        self.assertEqual(calc.minus(5, 2), 3)
        self.assertRaises(TypeError, calc.minus, "12", "22")

    def test_multiply(self):
        self.assertEqual(calc.multiply(5, 2), 10)
        self.assertRaises(TypeError, calc.multiply, "12", "22")

    def test_divide(self):
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertRaises(TypeError, calc.divide, "12", "22")
        self.assertRaises(ZeroDivisionError, calc.divide, 10, 0)
