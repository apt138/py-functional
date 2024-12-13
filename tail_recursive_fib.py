from functools import cache
import unittest


# check whether python interpreter supports tail recursive call stack
# tail recursive call stack = linear/fixed stack
@cache
def fib(n, acc=1):
    if n in (0, 1):
        return acc

    return fib(n - 1, n * acc)


class TestFib(unittest.TestCase):

    def test_sample_one(self):
        self.assertEqual(fib(5), 120)
        self.assertEqual(fib(4), 24)
        self.assertEqual(fib(3), 6)


if __name__ == "__main__":
    unittest.main()
