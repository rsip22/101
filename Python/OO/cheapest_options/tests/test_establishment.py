import unittest

from models import establishment


class EstablishmentTestCase(unittest.TestCase):

    """ Tests for the Establishment class."""

    def test_price_for_weekday_three_stars_establishment_regular_client(self):
        three_stars_price = establishment.Establishment(stars=3)
        self.assertEqual(110, int(three_stars_price.weekday_price))

    def test_price_for_weekday_three_stars_establishment_rewards_client(self):
        three_stars_price = establishment.Establishment(stars=3, is_rewards=True)
        self.assertEqual(80, int(three_stars_price.weekday_price))

    def test_price_for_weekend_three_stars_establishment_regular_client(self):
        three_stars_price = establishment.Establishment(stars=3)
        self.assertEqual(90, int(three_stars_price.weekend_price))

    def test_price_for_weekend_three_stars_establishment_rewards_client(self):
        three_stars_price = establishment.Establishment(stars=3, is_rewards=True)
        self.assertEqual(80, int(three_stars_price.weekend_price))

    def test_price_for_weekday_four_stars_establishment_regular_client(self):
        four_stars_price = establishment.Establishment(stars=4)
        self.assertEqual(160, int(four_stars_price.weekday_price))

    def test_price_for_weekday_four_stars_establishment_rewards_client(self):
        four_stars_price = establishment.Establishment(stars=4, is_rewards=True)
        self.assertEqual(110, int(four_stars_price.weekday_price))

    def test_price_for_weekend_four_stars_establishment_regular_client(self):
        four_stars_price = establishment.Establishment(stars=4)
        self.assertEqual(60, int(four_stars_price.weekend_price))

    def test_price_for_weekend_four_stars_establishment_rewards_client(self):
        four_stars_price = establishment.Establishment(stars=4, is_rewards=True)
        self.assertEqual(50, int(four_stars_price.weekend_price))

    def test_price_for_weekday_five_stars_establishment_regular_client(self):
        five_stars_price = establishment.Establishment(stars=5)
        self.assertEqual(220, int(five_stars_price.weekday_price))

    def test_price_for_weekday_five_stars_establishment_rewards_client(self):
        five_stars_price = establishment.Establishment(stars=5, is_rewards=True)
        self.assertEqual(100, int(five_stars_price.weekday_price))

    def test_price_for_weekend_five_stars_establishment_regular_client(self):
        five_stars_price = establishment.Establishment(stars=5)
        self.assertEqual(150, int(five_stars_price.weekend_price))

    def test_price_for_weekend_five_stars_establishment_rewards_client(self):
        five_stars_price = establishment.Establishment(stars=5, is_rewards=True)
        self.assertEqual(40, int(five_stars_price.weekend_price))


if __name__ == "__main__":
    unittest.main()
