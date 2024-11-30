"""
Using set comprehension, to determine the unique length of each word
in a given sentence after the punctuation   
"""

from string import punctuation
import re
import unittest


def replace_punctuation(string: str) -> str:
    return re.sub("[%s]" % re.escape(punctuation), "", string)


def get_unique_length(data: str) -> set[int]:
    if not data:
        return set()
    return {len(replace_punctuation(word)) for word in data.split()}


class TestSetComp(unittest.TestCase):

    def test_sample_one(self):
        result = get_unique_length("hello!!!")
        self.assertEqual(result, {5})

    def test_sample_two(self):
        result = get_unique_length("")
        self.assertEqual(result, set())

    def test_sample_three(self):
        result = get_unique_length("hello!, beautiful")
        self.assertSetEqual(result, {9, 5})

    def test_sample_four(self):
        result = get_unique_length("hello!, beautiful. how r u?")
        self.assertSetEqual(result, {9, 5, 1, 3})


if __name__ == "__main__":
    unittest.main()
