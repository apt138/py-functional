"""
A python program to determine if all words in a given list are palindromes.
The output should be boolean value:
    1. `True` if all words are palindromes
    2. `False` if atleast one word is not a palindrome

Contrainsts:
    1. Encouraged to use `map()` and `all()` functions.
    2. Assume the input list will only contains lowercase words without space or special characters.
"""

import unittest


def transform(words: list[str]) -> bool:
    return all(s == s[::-1] for s in words)


class TestPalindromeList(unittest.TestCase):
    def test_sample_one(self):
        words = ["radar", "level", "hello", "world", "deified"]
        result = transform(words)
        self.assertFalse(result)

    def test_sample_two(self):
        words = ["level", "radar"]
        result = transform(words)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
