"""
Description: A Dictionary with string keys and integer values.
    A function that transforms this dictonary based on the
    following criteria:

Criteria:
    1. The keys in the new dict should be reversed, i.e. abc->cba
    2. The values in the dict should be increased by 10 from the
    orginal values, i.e. 2->12

Assumptions:
    1. keys will always be string
    2. values will always be integer

Limitation:
    1. use `map`
"""

import unittest
from typing import Dict


def transform(data: Dict[str, int]) -> Dict[str, int]:
    if not data:
        return {}
    result = map(lambda x, y: (x[::-1], y + 10), data.keys(), data.values())
    return dict(list(result))


class TestTransform(unittest.TestCase):

    def test_sample_one(self):
        result = transform({"abc": 2, "def": 3})
        self.assertEqual(len(result), 2)
        self.assertEqual(list(result.keys()), ["cba", "fed"])
        self.assertEqual(list(result.values()), [12, 13])

    def test_sample_two(self):
        result = transform({})
        self.assertEqual(len(result), 0)
        self.assertEqual(list(result.keys()), [])
        self.assertEqual(list(result.values()), [])

    def test_sample_three(self):
        result = transform({"python": 6})
        self.assertEqual(len(result), 1)
        self.assertEqual(list(result.keys()), ["nohtyp"])
        self.assertEqual(list(result.values()), [16])


if __name__ == "__main__":
    unittest.main()
