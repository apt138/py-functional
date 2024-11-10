"""
A High Order Function: HOF, takes functions as input,
returns modified version of output (multiplied by 2)
"""

from typing import Callable
from operator import add, mul, sub, truediv
import unittest


def double(func: Callable) -> Callable:

    def wrapper(*args, **kwargs) -> float:
        return func(*args, **kwargs) * 2

    return wrapper


class TestDouble(unittest.TestCase):

    def test_double_add(self):
        double_add = double(add)
        result = double_add(2, 5)
        self.assertEqual(result, 14)

    def test_double_sub(self):
        double_sub = double(sub)
        result = double_sub(2, 5)
        self.assertEqual(result, -6)

    def test_double_mul(self):
        double_mul = double(mul)
        result = double_mul(2, 5)
        self.assertEqual(result, 20)

    def test_double_div(self):
        double_div = double(truediv)
        result = double_div(5, 2)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
