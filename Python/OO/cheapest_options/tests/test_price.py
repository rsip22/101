import unittest

from models import price, reservation_date


class PriceTestCase(unittest.TestCase):

    """ Tests for the Price class. """

    def setUp(self):
        self.is_rewards = False
        self.reservation_dates = reservation_date.ReservationDate(["16Mar2009(mon)",
                                                                   "17Mar2009(tues)",
                                                                   "18Mar2009(wed)"])

    def test_can_create_the_three_establishment_objects(self):
        establishment_objects = price.Price(self.reservation_dates, self.is_rewards)
        self.assertEqual(3, len(establishment_objects.establishments_list))

    def test_calculate_price_per_establishment(self):
        establishment_objects = price.Price(self.reservation_dates, self.is_rewards)
        price_per_establishment = establishment_objects._calculate_price_per_establishment()

        self.assertEqual(3, len(price_per_establishment))
        self.assertEqual(330, price_per_establishment[0]["price"])
        self.assertEqual("Econômico", price_per_establishment[0]["name"])

        self.assertEqual(480, price_per_establishment[1]["price"])
        self.assertEqual("Médio", price_per_establishment[1]["name"])

        self.assertEqual(660, price_per_establishment[2]["price"])
        self.assertEqual("Esbanjar", price_per_establishment[2]["name"])

    def test_get_cheapest_establishment(self):
        establishment_objects = price.Price(self.reservation_dates, self.is_rewards)
        cheapest_establishment = establishment_objects._get_cheapest_establishment()

        self.assertEqual("Econômico", cheapest_establishment["name"])


if __name__ == "__main__":
    unittest.main()
