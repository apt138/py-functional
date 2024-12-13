import unittest


def binary_search(arr: list[int], key: int) -> int:
    def recursive_search(low: int, high: int) -> int:
        if high >= low:
            mid = (low + high) // 2
            if key == arr[mid]:
                return mid
            if key > arr[mid]:
                return recursive_search(mid + 1, high)
            if key < arr[mid]:
                return recursive_search(low, mid - 1)

        return -1

    return recursive_search(0, len(arr) - 1)


class TestBinarySearch(unittest.TestCase):

    def test_sample_one(self):
        arr = [1, 2, 3, 4, 5]
        key = 3
        result = binary_search(arr, key)
        self.assertEqual(result, 2)

    def test_sample_two(self):
        arr = [1, 2, 3, 4, 5]
        key = 2
        result = binary_search(arr, key)
        self.assertEqual(result, 1)

    def test_sample_three(self):
        arr = [1, 2, 3, 4, 5]
        key = 4
        result = binary_search(arr, key)
        self.assertEqual(result, 3)

    def test_sample_four(self):
        arr = [1, 2, 3, 4, 5]
        key = 40
        result = binary_search(arr, key)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
