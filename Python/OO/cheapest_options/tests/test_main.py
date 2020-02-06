import unittest

import main


class MainTestCase(unittest.TestCase):

    """ Tests for the main module."""

    def test_run_with_weekday_input_returns_cheapest(self):
        input_data = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        self.assertEqual("Econômico", main.run(input_data))

    def test_run_with_mixed_days_input_returns_cheapest(self):
        input_data = "Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"
        self.assertEqual("Médio", main.run(input_data))

    def test_run_with_mixed_days_and_rewards_input_returns_cheapest_highest_category(self):
        input_data = "Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"
        self.assertEqual("Esbanjar", main.run(input_data))


if __name__ == "__main__":
    unittest.main()
