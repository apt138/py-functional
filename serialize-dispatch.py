from functools import singledispatch
import json
import csv
from io import StringIO
import unittest
from unittest.mock import patch


@singledispatch
def serialize(data):
    """Base dispatch funtion for serialize"""
    raise TypeError("Type not serializable.")


@serialize.register(dict)
def _(data: dict):
    """Dispatch function to handle dict variant"""
    print("Serializing as JSON")
    return json.dumps(data)


@serialize.register(list)
def _(data: list[tuple]):
    """Dispatch function to handle list"""
    print("Serializing as CSV")
    # StringIO() is file-like in-memory python object
    with StringIO() as output:
        writer = csv.writer(output)
        writer.writerows(data)
        return output.getvalue()


class TestSerializeDispatch(unittest.TestCase):

    def test_base(self):
        with self.assertRaises(TypeError) as context:
            serialize({1, 2, 3})

        self.assertTrue("type not serializable" in str(context.exception).lower())

    @patch("sys.stdout", new_callable=StringIO)
    def test_json(self, mock_stdout):
        result = serialize({"name": "apt", "job": "software engineer"})
        expected_stdout = mock_stdout.getvalue()
        self.assertTrue("Serializing as JSON" in expected_stdout)
        self.assertEqual('{"name": "apt", "job": "software engineer"}', result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_csv(self, mock_stdout):
        result = serialize([("name", "job"), ("apt", "software engineer")])
        expected_stdout = mock_stdout.getvalue()
        self.assertTrue("Serializing as CSV" in expected_stdout)
        self.assertEqual("name,job\r\napt,software engineer", result.strip())


if __name__ == "__main__":
    unittest.main()
