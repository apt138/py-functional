import unittest


def truthy_counter():
    count: int = 0
    while True:
        received = yield count
        if received:
            count += 1


class TestTruthyCounter(unittest.TestCase):

    def test_sample_one(self):
        # getting the handle of truthy counter generator
        counter = truthy_counter()

        # priming the generator
        # by calling next() func, making the counter to reach the first yield keyword
        # this generators yields current count, and and waits for next input
        # we get count value on below invocation
        count = next(counter)

        # assert whether it eq. zero
        self.assertEqual(count, 0)

        # send falsy value and check whether counter should not have incremented the count
        # in other words, it should stay the same value of zero.
        count = counter.send("")
        self.assertEqual(count, 0)

        # send truthy value and check whether counter should have updated the value by 1
        count = counter.send("hey!!")
        self.assertEqual(count, 1)


if __name__ == "__main__":
    unittest.main()
