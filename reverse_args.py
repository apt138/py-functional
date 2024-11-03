"""
Function that takes a function func and returns a new function.
The returned function should take two arguments and invoke func with its arguments reveresed.
"""

from typing import Callable
import unittest


def subtract(x: float, y: float) -> float:
    return x - y


def reverse_args(func: Callable[[float, float], float]) -> Callable:
    def inner(x: float, y: float):
        return func(y, x)

    return inner


class TestFunction(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(15, 10), 5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(10, 10), 0)

    def test_reverse_subtract(self):
        reverse_substract = reverse_args(subtract)
        self.assertEqual(reverse_substract(5, 10), 5)
        self.assertEqual(reverse_substract(15, 10), -5)
        self.assertEqual(reverse_substract(0, 0), 0)
        self.assertEqual(reverse_substract(10, 10), 0)


if __name__ == "__main__":
    unittest.main()
