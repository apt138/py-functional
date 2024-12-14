from functools import wraps
from typing import Callable
import unittest


def memoize(func: Callable) -> Callable:
    cache: dict = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


class TestMemoizeAckermann(unittest.TestCase):

    def test_sample_one(self):
        result = ackermann(3, 6)
        self.assertEqual(result, 509)


if __name__ == "__main__":
    unittest.main()
