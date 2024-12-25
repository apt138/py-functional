import unittest


def fibnocci(n, memo={}):
    # base case: n <= 1, then n
    if n <= 1:
        return n

    # using cache
    if n in memo:
        return memo[n]

    # if not in cache, make calculation and store in cache
    result = fibnocci(n - 1, memo) + fibnocci(n - 2, memo)
    memo[n] = result
    return result


class TestFibnocci(unittest.TestCase):

    def test_sample_one(self):
        result = fibnocci(2)
        self.assertEqual(result, 1)

    def test_sample_two(self):
        result = fibnocci(30)
        self.assertEqual(result, 832040)


if __name__ == "__main__":
    unittest.main()
