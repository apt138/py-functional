"""
Given a list of dictionaries, where each dictionary contains 
exactly one key-value pair. The task is to combine all these
dictionaries into a single dictionary without losing any key-value
pair.
"""

from typing import Dict, List
from functools import reduce
import unittest


def transform(data: List[Dict[str, int]]) -> Dict[str, int]:
    if not isinstance(data, list):
        raise ValueError("Data must be of list of dictionaries")
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Data must be of list of dictionaries")

    return reduce(lambda acc, cur: acc | cur, data)


class TestReduce(unittest.TestCase):

    def test_sample_one(self):
        with self.assertRaises(ValueError) as context:
            transform({"data": 1})

        self.assertTrue(
            "Data must be of list of dictionaries" in str(context.exception)
        )

    def test_sample_two(self):
        with self.assertRaises(ValueError) as context:
            transform([{"a": 1}, "string"])

        self.assertTrue(
            "Data must be of list of dictionaries" in str(context.exception)
        )

    def test_sample_three(self):
        excepted_result = {"a": 1, "b": 2}
        input_data = [{"a": 1}, {"b": 2}]
        result = transform(input_data)
        self.assertEqual(result, excepted_result)

    def test_sample_four(self):
        excepted_result = {"a": 1}
        input_data = [{"a": 1}]
        result = transform(input_data)
        self.assertEqual(result, excepted_result)


if __name__ == "__main__":
    unittest.main()
