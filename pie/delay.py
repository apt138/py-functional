"""
A placeholder function `download(user_id, resource)` that simulates
the generation of a download link.(for our purposes, we can simply use
uuid() or random alphanumeric string)

A decorator that progressively slows down the downloads for a given
user by doubling the time it takes the download link to be generated.
the first innovation happens instantly, the second one takes 1 second,
the third 2 second, the fourth 4 seconds and so on.
"""

from uuid import uuid4
from functools import wraps
from typing import Callable
from collections import defaultdict
from time import sleep
import unittest
from unittest.mock import patch
from io import StringIO
from re import findall


def delay(func: Callable) -> Callable:
    tracker = defaultdict(lambda: -1)

    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id, _ = args
        count = tracker[user_id]
        duration = pow(2, count) if count >= 0 else 0
        tracker[user_id] = count + 1
        if duration:
            print(f"your download will start in `{duration}`s")
        sleep(duration)
        return func(*args, **kwargs)

    return wrapper


@delay
def download(user_id, resource):
    return f"example.com/{uuid4()}"


class TestDelay(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_one(self, mock_stdout):
        result = download(3, "resource")
        printed_stdout = mock_stdout.getvalue()
        self.assertEqual(printed_stdout, "")
        self.assertIn("example.com/", result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_two(self, mock_stdout):
        download(1, "resource")
        result = download(2, "resource")
        printed_stdout = mock_stdout.getvalue()
        self.assertEqual(printed_stdout, "")
        self.assertIn("example.com/", result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_three(self, mock_stdout):
        download(3, "resource")
        result = download(4, "resource")
        printed_stdout = mock_stdout.getvalue()
        self.assertTrue(printed_stdout != "")
        durations = findall(r"`(.+?)`", printed_stdout)
        self.assertEqual(len(durations), 1)
        self.assertIn("example.com/", result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_four(self, mock_stdout):
        download(13, "resource")
        download(13, "resource")
        result = download(13, "resource")
        printed_stdout = mock_stdout.getvalue()
        self.assertTrue(printed_stdout != "")
        durations = findall(r"`(.+?)`", printed_stdout)
        self.assertEqual(len(durations), 2)
        self.assertIn("example.com/", result)


if __name__ == "__main__":
    unittest.main()
