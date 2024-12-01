import unittest
from datetime import datetime


def read_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


def filter_errors(lines):
    for line in lines:
        if "error" in line.lower():
            yield line


def parse_errors(lines):
    for line in lines:
        date, time, log = line.split(" ", 2)
        yield date, time, log


class TestEfficientLogParsing(unittest.TestCase):

    def test_sample_one(self):
        filename = "sample/logfile.log"
        lines = read_lines(filename)
        errors = filter_errors(lines)
        logs = parse_errors(errors)

        for date, time, log in logs:
            self.assertTrue(datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S"))
            self.assertTrue("error" in log.lower())


if __name__ == "__main__":
    unittest.main()
