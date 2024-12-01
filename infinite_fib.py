import unittest
from collections import deque

# def fib():
#     a, b = 0, 1
#     cur = None
#     yield a
#     yield b
#     while True:
#         cur = a + b
#         a = b
#         b = cur
#         yield cur


def fibnocci(start_points: tuple[int] = (0, 1)):
    a, b = start_points
    while True:
        yield a
        # below implemenation is incorrect, since repointed a, by the time
        # second assignment happens, we basically, saying b = 2b.
        # beacause a = b, this case requires a temp var
        # a = b
        # b = a + b

        # current equivalent implementation
        # temp = a
        # a = b
        # b = temp + b
        a, b = b, a + b


def fib_slide_window(
    n: int, window_size: int = 3, start_points: tuple[int] = (0, 1)
) -> None:
    window = deque(maxlen=window_size)
    fib = fibnocci(start_points)

    for number in fib:
        window.append(number)
        if len(window) == window_size:
            print(window_size)
            if window[-1] >= n:
                break


class TestInfiniteFibnocci(unittest.TestCase):

    def test_sample_one(self):
        fib = fibnocci()
        result = tuple(next(fib) for _ in range(5))
        self.assertEqual(result, (0, 1, 1, 2, 3))

    def test_sample_two(self):
        fib = fibnocci()
        result = tuple(next(fib) for _ in range(10))
        self.assertEqual(result, (0, 1, 1, 2, 3, 5, 8, 13, 21, 34))

    def test_sample_three(self):
        fib = fibnocci(start_points=(10, 12))
        result = tuple(next(fib) for _ in range(5))
        self.assertEqual(result, (10, 12, 22, 34, 56))


if __name__ == "__main__":
    unittest.main()
