"""
A Python program that merges two dictionaries, summing the values of common keys.
The program should work with any 2 dictionaries containing numeric values and
should include keys from both dictionaries in the final output  
"""

from copy import deepcopy
import unittest


def merge(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:

    if not isinstance(d1, dict):
        raise TypeError("inputs must be of dictionaries")
    if not isinstance(d2, dict):
        raise TypeError("inputs must be of dictionaries")

    if d1 and d2:
        all_keys = d1.keys() | d2.keys()
        return {k: d1.get(k, 0) + d2.get(k, 0) for k in all_keys}
    if d1 == {} and d2 == {}:
        return {}
    return deepcopy(d1 or d2)


class TestMergeDict(unittest.TestCase):

    def test_sample_one(self):
        d1 = {}
        d2 = {"a": 10, "b": 5}
        result = merge(d1, d2)
        self.assertDictEqual(result, d2)

    def test_sample_two(self):
        d1 = {"a": 10, "b": 5}
        d2 = {}
        result = merge(d1, d2)
        self.assertDictEqual(result, d1)

    def test_sample_three(self):
        self.assertDictEqual(merge({}, {}), {})

    def test_sample_four(self):
        with self.assertRaises(TypeError) as first_context:
            merge("testing", {"b": 2})

        with self.assertRaises(TypeError) as second_context:
            merge({"b": 5}, "testing")

        self.assertTrue(
            "inputs must be of dictionaries" in str(first_context.exception)
        )
        self.assertTrue(
            "inputs must be of dictionaries" in str(second_context.exception)
        )

    def test_sample_five(self):
        d1 = {"a": 10, "b": 5}
        d2 = {"b": 5, "c": 5}
        result = merge(d1, d2)
        self.assertDictEqual(result, {"a": 10, "b": 10, "c": 5})

    def test_sample_six(self):
        d1 = {"a": 10, "b": 5}
        d2 = {"c": 5}
        result = merge(d1, d2)
        self.assertDictEqual(result, {"a": 10, "b": 5, "c": 5})


if __name__ == "__main__":
    unittest.main()
