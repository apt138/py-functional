from statistics import mean
import re
from unittest.mock import patch
from io import StringIO
import unittest


def avg(*args, round_to: int) -> float:
    mu = mean(args)
    n = len(args)
    rounded_mu = round(mu, round_to)
    print(f"Count: `{n}`; Rounded Avg:`{rounded_mu}`")
    return rounded_mu


class TestAvgVariadic(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_one(self, mock_stdout):
        result = avg(10, 15, 10, 15, round_to=2)
        expected_stdout = mock_stdout.getvalue()
        expected_array = re.findall(r"`(.+?)`", expected_stdout)
        count, rounded_avg = tuple(map(float, expected_array))
        self.assertEqual(count, 4)
        self.assertEqual(result, rounded_avg)
        self.assertEqual(result, 12.5)


if __name__ == "__main__":
    unittest.main()
