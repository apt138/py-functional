from functools import partial
from typing import Callable
import unittest
from unittest.mock import patch
from io import StringIO


def send_mail(sender: str, recipient: str, subject: str, message: str) -> None:
    print(f"From: `{sender}`")
    print(f"To: `{recipient}`")
    print(f"Subject: `{subject}`")
    print(f"Message: `{message}`")


update_for: Callable = partial(
    send_mail,
    sender="noreply@example.com",
    subject="Daily Update",
)


class TestCurrying(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_one(self, mock_stdout):
        update_for(recipient="hey@apt.com", message="hello world")
        result = mock_stdout.getvalue()
        self.assertTrue("noreply@example.com" in result)
        self.assertTrue("Daily Update" in result)
        self.assertTrue("hey@apt.com" in result)
        self.assertTrue("hello world" in result)


if __name__ == "__main__":
    unittest.main()
