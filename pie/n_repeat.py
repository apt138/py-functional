"""
A `repeact` decorator, that invokes a given function any n number
of times.

the `repeat` decorator should work with any function that returns
numeric values. it should accept an argument that specifies the
number of time the decorated function is invoked, and returns a
list of the numbers returned in sorted order.
"""

from functools import wraps
from random import randint
import unittest


def repeat(n=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return sorted(func(*args, **kwargs) for _ in range(n))

        return wrapper

    return decorator


class TestNRepeat(unittest.TestCase):
    def test_sample_one(self):
        num = 7

        @repeat(n=num)
        def lotto_draws(start, end):
            return randint(start, end)

        lower = 10
        upper = 100
        result = lotto_draws(lower, upper)
        self.assertEqual(len(result), num)
        for num in result:
            self.assertTrue(lower <= num <= upper)

    def test_sample_two(self):
        num = 5

        @repeat(n=num)
        def lotto_draws(start, end):
            return randint(start, end)

        lower = 10
        upper = 50
        result = lotto_draws(lower, upper)
        self.assertEqual(len(result), num)
        for num in result:
            self.assertTrue(lower <= num <= upper)


if __name__ == "__main__":
    unittest.main()
