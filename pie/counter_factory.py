"""
A `create_counter` that returns a `counter` function that retains
its own state, i.e a closure.

the `counter` function should increment that count each time it
is called, before returning it.
"""

from typing import Callable
import unittest


def creater_counter(start: int = 0) -> Callable[[int], int]:
    tracker = [start]

    def counter(step: int = 1) -> int:
        tracker.append(tracker[-1] + step)
        return tracker[-1]

    return counter


class TestCounter(unittest.TestCase):
    def test_sample_one(self):
        counter = creater_counter()
        counter()  # 1
        result = counter()  # 2
        self.assertEqual(result, 2)

    def test_sample_two(self):
        counter = creater_counter(10)
        counter()  # 11
        result = counter()  # 12
        self.assertEqual(result, 12)

    def test_sample_three(self):
        counter = creater_counter()
        counter(2)  # 2
        result = counter(2)  # 4
        self.assertEqual(result, 4)

    def test_sample_four(self):
        counter = creater_counter(5)
        counter(2)  # 7
        result = counter()  # 8
        self.assertEqual(result, 8)


if __name__ == "__main__":
    unittest.main()
