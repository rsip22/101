import random

from constants import PRICE_TABLE
from enums import client


class Establishment:
    """
    Class for an establishment in the chain.

    Attributes:
        name: (str) name of the establishment
        stars: (int) establishment category
        is_rewards: (bool) establishment client participates in the rewards program
    """

    REGULAR = client.ClientType.REGULAR.value
    REWARDS = client.ClientType.REWARDS.value

    def __init__(self, stars, is_rewards=False):
        self.is_rewards = is_rewards
        self.stars = stars
        self.name = self._get_establishment_name()
        self.weekday_price = self._get_weekday_price()
        self.weekend_price = self._get_weekend_price()

    def _get_weekday_price(self):
        if not self.is_rewards:
            return PRICE_TABLE[self.stars]["weekday"][self.REGULAR]
        return PRICE_TABLE[self.stars]["weekday"][self.REWARDS]

    def _get_weekend_price(self):
        if not self.is_rewards:
            return PRICE_TABLE[self.stars]["weekend"][self.REGULAR]
        return PRICE_TABLE[self.stars]["weekend"][self.REWARDS]

    def _get_establishment_name(self):
        establishment_for_category = PRICE_TABLE[self.stars]["establishment"]
        return random.choice(establishment_for_category)

    def __str__(self):
        return self.name
