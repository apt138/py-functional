"""
TODO: to create a set of all prime numbers less than given number n;
"""

import unittest


# def is_prime(n):
#     for i in range(2, n + 1):
#         if n % i == 0 and i != n:
#             return False

#     return True


def is_prime(n):
    # Alternative
    # return not any(n % i == 0 for i in range(2, int(pow(n, 0.5)) + 1))
    return all(
        False if n % i == 0 and i != n else True for i in range(2, int(pow(n, 0.5)) + 1)
    )


def primes(n: int) -> set[int]:
    if n <= 1:
        raise ValueError("Prime numbers start at 2.")

    return {i for i in range(2, n) if is_prime(i)}


class TestPrimes(unittest.TestCase):

    def test_sample_one(self):
        with self.assertRaises(ValueError) as context:
            primes(0)

        self.assertTrue("Prime numbers start at 2" in str(context.exception))

    def test_sample_two(self):
        result = primes(3)
        self.assertSetEqual(result, {2})

    def test_sample_three(self):
        result = primes(10)
        self.assertSetEqual(result, {2, 3, 5, 7})

    def test_sample_four(self):
        result = primes(15)
        self.assertSetEqual(result, {2, 3, 5, 7, 11, 13})


if __name__ == "__main__":
    unittest.main()
