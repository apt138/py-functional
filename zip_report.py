"""
A  comprehensive report that showcases items, their prices and available colors.
    1. items - list of product names
    2. prices - list of prices corresponding to the items
    3. colors - list of available for each item (some items might
    not have any associated colors)
    4. discounts - list of discount percentages for each item during
    a sale  (0 if no discount)
"""

# TODO: Instructions
#  1. use the zip function to combine items, prices, colors
# and discounts into a list of tuples. Each tuple should represent
# a product in the store

# 2. Ensure the length of items, prices, colors and discounts are eqaul
# using the strict mode of zip. if not, raise a relvant error.

# 3. For each product, calculate its discounted price and append this to
# the tuple. The formula is price = price x (1-discount/100). The prices
# and discounts should be rounded off to 2 decimal plaeces

# 4. Finally, build a report where the keys are the item names, and
# the value is another dictinary containing: price, available colors
# discount price

import unittest

items: list[str] = ["Shirt", "Pants", "Shoes", "Hat"]
prices: list[float] = [20.00, 30.00, 50.00, 10.00]
colors: list[str] = ["Red", "Blue", None, "Black"]
discounts: list[int] = [10, 0, 20, 5]

# output
# {
#     "Shirt": {
#         "Price": 20.00,
#         "Available Colors": "Red",
#         "Discounted Price": 18.00,
#     },
#     "Pants": {
#         "Price": 30.00,
#         "Available Colors": "Blue",
#         "Discounted Price": 30.00,
#     },
#     "Shoes": {
#         "Price": 50.00,
#         "Available Colors": None,
#         "Discounted Price": 40.00,
#     },
#     "Hat": {
#         "Price": 10.00,
#         "Available Colors": "Black",
#         "Discounted Price": 9.50,
#     },
# }


def calc_discount_price(price: float, discount_percent: float) -> float:
    return round(price * (1 - (discount_percent / 100)), 2)


def transform(items, prices, colors, discounts):
    try:
        for item, price, color, discount in zip(
            items,
            prices,
            colors,
            discounts,
            strict=True,
        ):
            heading: tuple[str] = ("Price", "Available Colors", "Discount Price")
            product = dict(
                zip(
                    heading,
                    (
                        price,
                        color,
                        calc_discount_price(price, discount),
                    ),
                )
            )
            yield {item: product}
    except ValueError:
        raise ValueError("All input lists must have the same length")


class TestZipReport(unittest.TestCase):
    def test_sample_one(self):
        items = ["Shirt"]
        prices = [100]
        colors = ["red"]
        discounts = [10]

        result = next(transform(items, prices, colors, discounts))
        expected_result = {
            "Shirt": {"Price": 100, "Available Colors": "red", "Discount Price": 90}
        }

        self.assertEqual(result, expected_result)

    def test_sample_two(self):
        items = ["Shirt"]
        prices = [100]
        colors = ["red"]
        discounts = [10, 12]

        with self.assertRaises(ValueError) as context:
            list(transform(items, prices, colors, discounts))

        self.assertEqual(
            "All input lists must have the same length", str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
