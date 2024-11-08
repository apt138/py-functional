# converting below function to pure function that deals with immutable data
from typing import List, Callable
import unittest


def increase_elements(data: List[int], value: int) -> List[int]:
    for i in range(len(data)):
        data[i] += value

    return data


def add_x(x: int) -> Callable[[int], int]:
    def inner(y: int) -> int:
        return x + y

    return inner


def increase_elements_pure(data: List[int], value: int) -> List[int]:
    add_v = add_x(value)
    return list(map(add_v, data))


class TestImpureIncreaseElements(unittest.TestCase):

    def test_side_effects(self):
        test_list = [1, 2, 3]
        result = increase_elements(test_list, 3)
        self.assertEqual(test_list, [4, 5, 6])
        self.assertEqual(result, [4, 5, 6])


class TestPureIncreaseElements(unittest.TestCase):

    def test_no_side_effects(self):
        test_list = [1, 2, 3]
        result = increase_elements_pure(test_list, 3)
        self.assertEqual(result, [4, 5, 6])
        self.assertEqual(test_list, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
