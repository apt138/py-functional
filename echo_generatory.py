import unittest
from unittest.mock import patch
from io import StringIO


def echo():
    while True:
        # waits for input from .send()
        # otherwords, it consumes data
        received = yield

        # input received from last step
        print(f"you said: {received}")


class TestEchoGenerator(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_one(self, mock_stdout):
        # Getting the handle of echo generator
        gen = echo()

        # priming the generator
        # i.e, after the invocation, func won't reach the first yield keyword
        # so,we advancing the function, this is called priming
        # it is done by next()
        next(gen)

        # send data
        gen.send("hello world!")

        # confirm the msg printed to stdout
        expected = mock_stdout.getvalue()
        self.assertTrue("you said: hello world!" in expected)


if __name__ == "__main__":
    unittest.main()
