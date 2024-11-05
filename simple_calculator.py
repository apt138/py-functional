from operator import add, mul, sub, truediv
import unittest
from typing import Callable


allowed_operations = {
    "add": add,
    "subtract": sub,
    "multiply": mul,
    "divide": truediv,
}


def calc(
    operation: Callable[[float, float], float],
    a: float,
    b: float,
) -> float:
    if operation not in allowed_operations:
        return NotImplemented
    return allowed_operations[operation](a, b)


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc("add", 3, 2), 5)
        self.assertEqual(calc("add", -3, 2), -1)
        self.assertEqual(calc("add", 3, -3), 0)
        self.assertEqual(calc("add", 0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calc("subtract", 3, 1), 2)
        self.assertEqual(calc("subtract", 3, -1), 4)
        self.assertEqual(calc("subtract", -3, 1), -4)
        self.assertEqual(calc("subtract", 3, 3), 0)
        self.assertEqual(calc("subtract", 0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calc("multiply", 2, 3), 6)
        self.assertEqual(calc("multiply", 2, 0), 0)
        self.assertEqual(calc("multiply", 0, 3), 0)
        self.assertEqual(calc("multiply", 0, 0), 0)

    def test_divide(self):
        self.assertEqual(calc("divide", 2, 2), 1)
        self.assertEqual(calc("divide", 3, 2), 1.5)
        self.assertEqual(calc("divide", 3, 0.5), 6)
        with self.assertRaises(ZeroDivisionError) as context:
            calc("divide", 3, 0)
            self.assertTrue("division by zero" in context.exception)

    def test_unknown(self):
        self.assertEqual(calc("integrate", 2, 3), NotImplemented)


if __name__ == "__main__":
    unittest.main()
