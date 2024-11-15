"""
A decorator called logger that logs out the function name and args/kwargs
of the function it is applied  to as  well as the result that the 
function returns
"""

from functools import wraps
from typing import Callable
import unittest
from unittest.mock import patch
from io import StringIO


def logger(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: '{func.__name__}' with arguments:{args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result

    return wrapper


@logger
def add(a: float, b: float) -> float:
    return a + b


class TestLoggerDecorator(unittest.TestCase):

    # Patch stdout to capture print statements
    @patch("sys.stdout", new_callable=StringIO)
    def test_logger_decorater(self, mock_stdout):
        result = add(2, b=3)
        excepted_output = "Calling function: 'add' with arguments:(2,), {'b': 3}\nFunction 'add' returned: 5"
        printed_output = mock_stdout.getvalue()
        self.assertEqual(excepted_output.strip(), printed_output.strip())
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
