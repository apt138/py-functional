"""
A function `get_weather(city)` that stimulates the retrieval of weather
data for a given city. Use a delay of 1 second to mimic the real-time
delay of calling a live API.

A decorator `cache(func)` that checks if the requested city's weather data
is already in the cache AND it isn't too old. (i.e. less than 10 seconds old.)
If the data meets both conditions, the decorator should return a value from
cache rather than allow the innocation of the target function.

if the weather data for the city is not in the cache or it's too old. then
`get_weather(city)`  innocation should be allowed to get and return fresh data.
In addition, the cache should be updated with new data.

for simplicity, implement the weather data cache for each city as a dictionay.
"""

from functools import wraps
from random import randint
from time import sleep
from typing import Callable
import time
import unittest
from unittest.mock import patch
from io import StringIO


def cache(seconds=10):
    def decorator(func: Callable) -> Callable:
        data = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            city = args[0]
            city_data = data.get(city, {})
            if city_data and (time.time() - city_data.get("time")) <= seconds:
                print("Using data from cache.")
                return city_data.get("data")
            result: dict[str, float] = func(*args, **kwargs)
            data[city] = {"time": time.time(), "data": result}
            return result

        return wrapper

    return decorator


class TestCacheDecorator(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_one(self, mock_stdout):
        result = get_weather("chennai")
        printed_stdout = mock_stdout.getvalue()
        self.assertTrue("fetching" in printed_stdout.lower())
        self.assertTrue(isinstance(result, dict))
        self.assertTrue("temperature" in result)
        self.assertTrue("humidity" in result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_two(self, mock_stdout):
        result1 = get_weather("chennai")
        result2 = get_weather("chennai")
        printed_stdout = mock_stdout.getvalue()
        self.assertTrue("cache" in printed_stdout.lower())
        self.assertEqual(result1, result2)
        self.assertTrue(isinstance(result1, dict))
        self.assertTrue(isinstance(result2, dict))
        self.assertTrue("temperature" in result2)
        self.assertTrue("humidity" in result2)

    @patch("sys.stdout", new_callable=StringIO)
    def test_sample_three(self, mock_stdout):
        result1 = get_weather("chennai")
        result2 = get_weather("bangalore")
        printed_stdout = mock_stdout.getvalue()
        self.assertTrue("fetching" in printed_stdout.lower())
        self.assertNotEqual(result1, result2)
        self.assertTrue(isinstance(result1, dict))
        self.assertTrue(isinstance(result2, dict))
        self.assertTrue("temperature" in result2)
        self.assertTrue("humidity" in result2)


@cache(seconds=7)
def get_weather(city: str) -> dict[str, float]:
    sleep(1)
    print(f"Fetching weather data for {city}...")
    temperature = randint(-10, 30)
    humidity = randint(0, 100)
    return dict(temperature=temperature, humidity=humidity)


if __name__ == "__main__":
    unittest.main()
