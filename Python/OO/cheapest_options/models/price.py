from models import establishment
from helpers import helpers
from enums import stars


class Price:

    """Class for the price information for the establishments in the chain."""

    def __init__(self, reservation_dates, is_rewards):
        """
        :param reservation_dates: list with valid datetime objects
        :param is_rewards: boolean if the client belongs to the Rewards program
        """
        self._dates = reservation_dates
        self.establishments_list = self._create_establishments_list(is_rewards)
        self._price_per_establishment = self._calculate_price_per_establishment()
        self.cheapest = self._get_cheapest_establishment()

    def _create_establishments_list(self, is_rewards):
        """ Instantiate an establishment object for each service category.

        :param is_rewards: boolean if the client belongs to the Rewards program
        :return: a list with Establishment objects
        """
        establishments_list = []
        for star in stars.Stars:
            establishments_list.append(establishment.Establishment(stars=star.value, is_rewards=is_rewards))
        return establishments_list

    def _calculate_price_per_establishment(self):
        """ Calculate the total price per establishment in the establishments_list.

        :return: a list with establishment objects containing the total price for the reservation,
                 for each of them.
        """
        establishments = []
        for item in self.establishments_list:
            establishment_price = dict()
            establishment_price["name"] = item.name
            establishment_price["stars"] = item.stars
            establishment_price["price"] = helpers.calculate_price_per_category(item, self._dates)
            establishments.append(establishment_price)
        return establishments

    def _get_cheapest_establishment(self):
        """ Find the cheapest establishment.

        :param establishment_list: a list of Establishment objects with prices to be compared
        :return: Establishment object with the cheapest reservation total
        """
        first_item = 0
        cheapest = self._price_per_establishment[first_item]
        cheapest_value = cheapest["price"]

        for item in self._price_per_establishment:
            if item["price"] < cheapest_value:
                cheapest = item
                cheapest_value = item["price"]
            elif item["price"] == cheapest_value:
                if item["stars"] > cheapest["stars"]:
                    cheapest = item
                    cheapest_value = item["price"]
        return cheapest
