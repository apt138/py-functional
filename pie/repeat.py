"""
A decorator called `repeat` that invokes a function of
variables/unknow arity twice.

then, define a function called `lotto_draws` that takes
start and end arguments, returns an integer that is
randomly drawn from that range(inclusively)

decorate `lotto_draws` with `repeat` to get 2 random numbers
"""

from random import randint
from typing import Callable
from functools import wraps
import unittest
from unittest.mock import patch
from re import findall
from io import StringIO


def repeat(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        for _ in range(2):
            result = func(*args, **kwargs)
            print(f"Randonly drawn number: {result}")

    return wrapper


@repeat
def lotto_draws(start: int, end: int) -> int:
    return randint(start, end)


class TestRepeat(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_one(self, mock_stdout):
        lower = 0
        upper = 10
        lotto_draws(lower, upper)
        printed_output = mock_stdout.getvalue()
        self.assertTrue("Randonly drawn number" in printed_output)
        draws = findall(r"\d", printed_output)
        for num in draws:
            self.assertTrue(lower <= int(num) <= upper)


if __name__ == "__main__":
    unittest.main()
