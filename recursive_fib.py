from functools import cache
import unittest


@cache
def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


class TestFib(unittest.TestCase):

    def test_sample_one(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(10), 55)


if __name__ == "__main__":
    unittest.main()
