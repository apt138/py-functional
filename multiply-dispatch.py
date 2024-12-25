from functools import singledispatch
import unittest
from unittest.mock import patch
import re
from io import StringIO


@singledispatch
def mul(a, b):
    """Base function"""
    raise NotImplementedError("Unsupported types.")


@mul.register(int)
def _(a, b):
    """Function for integer multiplication"""
    # single dispatch will only look type of arg.
    # its developer responsibilty to type check the second arg
    if not isinstance(b, int):
        raise NotImplementedError("Both should be of same type.")
    print("using `int` func definition")
    return a * b


@mul.register(float)
def _(a, b):
    if not isinstance(b, float):
        raise NotImplementedError("Both should be of same type.")
    print("using `float` func definition")
    return round(a * b, 3)


@mul.register(str)
def _(a, b):
    if not isinstance(b, str):
        raise NotImplementedError("Both should be of same type.")
    print("using `str` func definition")
    # custom user definition
    return f"{a}{b}" * len(b)


class TestMulSingeDispatch(unittest.TestCase):

    def test_base(self):
        with self.assertRaises(NotImplementedError) as context:
            mul(["2", "3"], {"a": 2})

        self.assertTrue("Unsupported types" in str(context.exception))

    @patch("sys.stdout", new_callable=StringIO)
    def test_int(self, mock_stdout):
        result = mul(2, 3)
        expected_stdout = mock_stdout.getvalue()
        found = re.findall(r"`(.+?)`", expected_stdout)
        if not found:
            self.assertTrue(
                False, "The function failed to invoke int variant of multiple function"
            )
        func_used = found[0]
        self.assertEqual(func_used, "int")
        self.assertEqual(result, 6)

    @patch("sys.stdout", new_callable=StringIO)
    def test_float(self, mock_stdout):
        result = mul(10.0112345, 20.0)
        expected_stdout = mock_stdout.getvalue()
        found = re.findall(r"`(.+?)`", expected_stdout)
        if not found:
            self.assertTrue(
                False,
                "The function failed to invoke float variant of multiple function",
            )
        func_used = found[0]
        self.assertEqual(func_used, "float")
        self.assertEqual(result, 200.225)

    @patch("sys.stdout", new_callable=StringIO)
    def test_str(self, mock_stdout):
        result = mul("a", "pt")
        expected_stdout = mock_stdout.getvalue()
        found = re.findall(r"`(.+?)`", expected_stdout)
        if not found:
            self.assertTrue(
                False,
                "The function failed to invoke string variant of multiple function",
            )
        func_used = found[0]
        self.assertEqual(func_used, "str")
        self.assertEqual(result, "aptapt")


if __name__ == "__main__":
    unittest.main()
