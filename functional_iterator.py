from typing import Callable
import unittest


class FunctionalIterator:

    def __init__(self, func: Callable, start: int, end: int) -> None:
        self.func = func
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.func(self.current)
            self.current += 1
            return result
        else:
            raise StopIteration


class TestFunctionalIterator(unittest.TestCase):

    def test_sample_one(self):
        square = lambda x: pow(x, 2)
        my_iter = FunctionalIterator(square, 5, 8)
        self.assertEqual(next(my_iter), 25)
        self.assertEqual(next(my_iter), 36)
        self.assertEqual(next(my_iter), 49)

    def test_sample_two(self):
        cube = lambda x: pow(x, 3)
        my_iter = FunctionalIterator(cube, 2, 5)
        self.assertEqual(next(my_iter), 8)
        self.assertEqual(next(my_iter), 27)
        self.assertEqual(next(my_iter), 64)


if __name__ == "__main__":
    unittest.main()
