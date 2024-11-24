"""
Run-length encoding RLE is a basic form of lossless data compression
where sequence of identical data values (runs) are stored as a 
single data value and count.

input:
A String s containing uppercase alphabets (1<=len(s)<=1000).

output:
returns a run-length encoded version of the string, where each run
(sequences of the same character) is replaced by the character
followed by the number of times it appears consecutively

Example:
AABCCDEEEE -> A2B1C2D1E4
"""

from functools import reduce
import unittest


def transform(data: str) -> str:
    if not data:
        return ""

    # replicating the functionality of counter from collections
    counter = reduce(lambda acc, x: acc | {x: acc.get(x, 0) + 1}, data, {})

    # concat the items (key,value pairs)
    result = reduce(lambda acc, x: acc + "".join(map(str, x)), counter.items(), "")

    return result


# above func is not handling below scenario
# AABA => A2B1A1
# instead returns A3B1


def run_length_encode(data: str) -> str:
    if not data:
        return ""

    def reducer(acc: list[tuple[str, int]], char: str) -> list[tuple[str, int]]:
        if acc and char == acc[-1][0]:
            acc[-1] = (char, acc[-1][1] + 1)
        else:
            acc.append((char, 1))

        return acc

    counter = reduce(reducer, data, [])
    # concat the items (key,value pairs)
    result = "".join(f"{char}{count}" for char, count in counter)
    return result


class TestRunLengthEncode(unittest.TestCase):

    def test_sample_one(self):
        result = run_length_encode("AAACC")
        self.assertEqual(result, "A3C2")

    def test_sample_two(self):
        result = run_length_encode("AAA")
        self.assertEqual(result, "A3")

    def test_sample_three(self):
        result = run_length_encode("")
        self.assertEqual(result, "")

    def test_sample_four(self):
        result = run_length_encode("AABA")
        self.assertEqual(result, "A2B1A1")


if __name__ == "__main__":
    unittest.main()
