# A retry HOF that tries to execure another function a specified number of times

from random import randint
import unittest
from unittest.mock import patch


def unstable_function():
    "Simulates an unstable funtion that fails 50% of the time"
    if randint(0, 1) == 0:
        print("Function failed!!")
        raise ValueError("Transient error")

    else:
        print("Function succeeded!")
        return "Success!"


def retry_hof(func, max_retries=3):
    # loop until max_retries expires
    for _ in range(max_retries):
        # try to return the result of function invocation
        try:
            return func()
        # on ValueError, go to next iteration
        except ValueError:
            continue

    # return failure meessage if there is no success on first n(max_retries) attempts
    return "Failed after max retries"


class TestRetryHOF(unittest.TestCase):

    @patch("__main__.unstable_function")
    def test_retry_hof_succeeds_on_first_try(self, mock_func):
        # Mocking unstable_function to succeed on the first call
        mock_func.return_value = "Success!"

        # Run retry_hof with mocked function
        result = retry_hof(mock_func)

        # check if it returned "Success!" immediately
        self.assertEqual(result, "Success!")

        # Ensure mockfunction was called only once, since it was succeed on first attemp
        mock_func.assert_called_once()

    @patch("__main__.unstable_function")
    def test_retry_hof_succeeds_after_retries(self, mock_func):
        # mocking unstable_function to fail twice, and succeed on the third attempt
        mock_func.side_effect = [
            ValueError("Transient error"),
            ValueError("Transient error"),
            "Success!",
        ]

        # Run retry_hof with the mocked function
        result = retry_hof(mock_func)

        # check if it returned success after retries
        self.assertEqual(result, "Success!")

        # check if mockfunction was called three times (2 failures,1 success)
        self.assertEqual(mock_func.call_count, 3)

    @patch("__main__.unstable_function")
    def test_retry_hof_fails_after_retries(self, mock_func):
        # mocking unstable function to always raise an exception
        mock_func.side_effect = ValueError("Transient error")

        # run retry_hof with mocked function
        result = retry_hof(mock_func)

        # check if it returned the failure message
        self.assertEqual(result, "Failed after max retries")

        # check if the mockfunction was called three times (max_retries) before returning the failure message
        self.assertEqual(mock_func.call_count, 3)


if __name__ == "__main__":
    unittest.main()
