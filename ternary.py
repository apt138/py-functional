"""
A Single Lambda function `ternary` that simulates a
ternary operation to evaluate the sign of a given number.

The function takes a single argument (a number), will be
evaluated, returns one of three strings
a. `positive`
b. `negative`
c. `zero`
"""

import unittest

ternary = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"


class TestTernaryFunction(unittest.TestCase):

    def test_positive(self):
        result = ternary(1)
        self.assertEqual(result, "positive")

    def test_negative(self):
        result = ternary(-1)
        self.assertEqual(result, "negative")

    def test_zero(self):
        result = ternary(0)
        self.assertEqual(result, "zero")


if __name__ == "__main__":
    unittest.main()
