from statistics import mean
import unittest


def avg(*args, round_to: int = 3) -> float:
    mu = mean(args)
    return round(mu, round_to)


class TestAvg(unittest.TestCase):

    def test_sample_one(self):
        result = avg(1, 2, 3)
        self.assertEqual(result, 2)

    def test_sample_two(self):
        result = avg(2, 2, 3)
        self.assertEqual(result, 2.333)

    def test_sample_three(self):
        result = avg(2, 2, 3, round_to=1)
        self.assertEqual(result, 2.3)


if __name__ == "__main__":
    unittest.main()
