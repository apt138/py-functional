"""
TODO: transform list of customer dictionaries into list of customer names with active
      accounts who spent more than 100
"""

import unittest


def transform(data: list[dict]) -> list[str]:
    if not data:
        return []
    return [
        customer.get("name", "NA")
        for customer in data
        if customer.get("account_status") == "active"
        and customer.get("amount_spent") >= 100
    ]


class TestListComp(unittest.TestCase):

    def test_sample_one(self):
        data = [
            {"name": "Alice", "account_status": "active", "amount_spent": 150},
            {"name": "Bob", "account_status": "inactive", "amount_spent": 200},
            {"name": "Charlie", "account_status": "active", "amount_spent": 50},
            {"name": "Diana", "account_status": "active", "amount_spent": 100},
        ]
        result = transform(data)
        self.assertEqual(len(result), 2)
        self.assertEqual(result, ["Alice", "Diana"])

    def test_sample_two(self):
        self.assertEqual(transform([]), [])

    def test_sample_three(self):
        data = [{"name": "Alice", "account_status": "inactive", "amount_spent": 150}]
        self.assertEqual(transform(data), [])


if __name__ == "__main__":
    unittest.main()
