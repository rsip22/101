import unittest

from stock_price import open_and_close_prices


class TestOpenAndClosePrices(unittest.TestCase):

    def test_open_and_close_prices_on_weekend_returns_nothing(self):
        result = open_and_close_prices('1-January-2000', '31-December-2000', 'Sunday')
        self.assertIsNone(result)

    def test_open_and_close_prices_on_a_monday_returns_items(self):
        result = open_and_close_prices('17-January-2000', '22-February-2000', 'Monday')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 5)
        for item in result:
            self.assertIsNotNone(item['date'])
            self.assertGreater(item['open'], 0)
            self.assertGreater(item['close'], 0)

    def test_open_and_close_prices_on_a_wednesday_returns_items(self):
        result = open_and_close_prices('26-March-2001', '15-August-2001', 'Wednesday')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 17)
        for item in result:
            self.assertIsNotNone(item['date'])
            self.assertGreater(item['open'], 0)
            self.assertGreater(item['close'], 0)

    def test_open_and_close_prices_on_days_starting_with_a_digit(self):
        result = open_and_close_prices('6-January-2000', '25-January-2000', 'Thursday')
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
        for item in result:
            self.assertIsNotNone(item['date'])
            self.assertGreater(item['open'], 0)
            self.assertGreater(item['close'], 0)
