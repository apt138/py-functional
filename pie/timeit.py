"""
A decorator called `timeit` that meaures the amount of time
a given function takes to run and prints that out in seconds.
"""

from functools import wraps
from typing import Callable
from time import perf_counter
import unittest
from unittest.mock import patch
from io import StringIO
from re import findall


def timeit(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start: float = perf_counter()
        result = func(*args, **kwargs)
        end: float = perf_counter()
        template = "Function named `{}` took `{}` second(s) to execute."
        print(template.format(func.__name__, round(end - start, 3)))
        return result

    return wrapper


@timeit
def loop_many_times(n):
    for _ in range(n):
        continue


class TestTimeIt(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_one(self, mock_stdout):
        loop_many_times(10**7)
        printed_stdout = mock_stdout.getvalue()
        self.assertTrue("loop_many_times" in printed_stdout)
        _, duration = findall("`(.+?)`", printed_stdout)
        self.assertTrue(float(duration))


if __name__ == "__main__":
    unittest.main()
