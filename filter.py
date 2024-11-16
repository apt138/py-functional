"""
Given two lists of equal length, one called reference
containing binary values either 0 or 1 and another called 
values containing strings.

A function that returns a new list containing only those
strings from the values list where the positionally corresponding
value in the refreence list.

Assumptions:
1. the two input lists will always have equal length.
2. the reference list will only contains 0  and 1s
3. the values list will contains strings with length 1.
"""

import unittest
from collections import namedtuple

Pair = namedtuple("Pair", "select value")

reference: list[int] = [0, 1, 1, 0, 1, 0]
values: list[str] = list("abcdef")


def transform(ref: list[int], val: list[str]) -> list[str]:
    filtered_ref_val = filter(lambda x: x[0], zip(ref, val))
    filtered_val = map(lambda x: x[1], filtered_ref_val)
    return list(filtered_val)


def named_transform(ref: list[int], val: list[str]) -> list[str]:
    pairs = map(Pair, ref, val)
    return [p.value for p in pairs if p.select]


class TestTransform(unittest.TestCase):
    def test_sample_one(self):
        ref = [0, 1]
        val = ["a", "b"]
        result = transform(ref, val)
        self.assertEqual(len(result), 1)
        self.assertEqual(result, ["b"])

    def test_sample_two(self):
        ref = [0, 0]
        val = ["a", "b"]
        result = transform(ref, val)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

    def test_sample_three(self):
        ref = [1, 1]
        val = ["a", "b"]
        result = transform(ref, val)
        self.assertEqual(len(result), 2)
        self.assertEqual(result, val)

    def test_sample_four(self):
        ref = []
        val = []
        result = transform(ref, val)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, val)

    def test_sample_five(self):
        ref = [0, 1]
        val = ["a", "b"]
        result = named_transform(ref, val)
        self.assertEqual(len(result), 1)
        self.assertEqual(result, ["b"])

    def test_sample_six(self):
        ref = [0, 0]
        val = ["a", "b"]
        result = named_transform(ref, val)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

    def test_sample_seven(self):
        ref = [1, 1]
        val = ["a", "b"]
        result = named_transform(ref, val)
        self.assertEqual(len(result), 2)
        self.assertEqual(result, val)

    def test_sample_eight(self):
        ref = []
        val = []
        result = named_transform(ref, val)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, val)


if __name__ == "__main__":
    unittest.main()
