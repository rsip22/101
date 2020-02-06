import unittest
from datetime import datetime

from helpers import helpers


class HelpersTestCase(unittest.TestCase):

    """Tests for the helpers module."""

    def test_count_weekend_days_with_only_week_days_returns_zero(self):
        input_data = [datetime(2009, 3, 16, 0, 0),
                      datetime(2009, 3, 17, 0, 0),
                      datetime(2009, 3, 18, 0, 0)]
        count = helpers.count_weekend_days(input_data)
        self.assertEqual(count, 0)

    def test_count_weekend_days_with_one_weekend_day_and_two_week_days_returns_one(self):
        input_data = [datetime(2019, 11, 7, 0, 0),
                      datetime(2019, 11, 8, 0, 0),
                      datetime(2019, 11, 9, 0, 0)]
        count = helpers.count_weekend_days(input_data)
        self.assertEqual(count, 1)

    def test_count_weekend_days_with_three_weekend_days_returns_three(self):
        input_data = [datetime(2019, 11, 7, 0, 0),
                      datetime(2019, 11, 8, 0, 0),
                      datetime(2019, 11, 9, 0, 0),
                      datetime(2019, 11, 15, 0, 0),
                      datetime(2019, 11, 16, 0, 0),
                      datetime(2019, 11, 17, 0, 0)]
        count = helpers.count_weekend_days(input_data)
        self.assertEqual(count, 3)

    def test_parse_date_with_correct_date_format_should_parse(self):
        input_data = "16Mar2009(mon)"
        day = helpers.parse_date(input_data)
        self.assertEqual(day, ("16", "Mar", "2009"))

    def test_parse_date_with_correct_date_format_but_no_weekday_should_parse(self):
        input_data = "16Mar2009"
        day = helpers.parse_date(input_data)
        self.assertEqual(day, ("16", "Mar", "2009"))

    def test_parse_date_with_incorrect_date_format_raises_exception(self):
        input_data = "16Mar99"
        with self.assertRaises(AttributeError) as err:
            helpers.parse_date(input_data)

        # Assert that it informs that the input date is not valid.
        self.assertEqual(str(err.exception), "Cannot parse the date. Is the input date correct?")

    def test_parse_dates_with_correct_list_should_parse(self):
        input_data = ["16Mar2009(mon)", "17Mar2009(tues)", "18Mar2009(wed)"]
        parsed_dates = helpers.parse_dates(input_data)
        self.assertEqual([datetime(2009, 3, 16, 0, 0),
                          datetime(2009, 3, 17, 0, 0),
                          datetime(2009, 3, 18, 0, 0)], parsed_dates)

    def test_parse_dates_with_empty_list_raises_exception(self):
        input_data = []
        with self.assertRaises(ValueError):
            helpers.parse_dates(input_data)

    def test_parse_string_with_colon_splits_correctly_and_returns_list(self):
        input_data = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        parsed_str = helpers.parse_string(input_data, ":")
        self.assertEqual(parsed_str, ["Regular", "16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"])

    def test_parse_string_with_colon_splits_correctly_and_returns_list_empty_client(self):
        input_data = "16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"

        with self.assertRaises(SyntaxError) as err:
            helpers.parse_string(input_data, ":")
        self.assertEqual(str(err.exception), "Cannot parse the input. Is it in the correct format?")

    def test_parse_string_with_comma_splits_correctly_and_returns_list(self):
        input_data = "16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        parsed_str = helpers.parse_string(input_data, ",")
        self.assertEqual(parsed_str, ["16Mar2009(mon)", "17Mar2009(tues)", "18Mar2009(wed)"])

    def test_parse_string_with_wrong_delimiter_raises_exception(self):
        input_data = "16Mar2009(mon)/17Mar2009(tues)/18Mar2009(wed)"

        # Assert that it informs that the input date is not valid.
        with self.assertRaises(SyntaxError) as err:
            helpers.parse_string(input_data, ",")
        self.assertEqual(str(err.exception), "Cannot parse the input. Is it in the correct format?")

    def test_parse_weekday_with_three_letters_day(self):
        input_data = "16Mar2009(mon)"
        day = helpers.parse_weekday(input_data)
        self.assertEqual(day, "mon")

    def test_parse_weekday_with_four_letters_day(self):
        input_data = "17Mar2009(tues)"
        day = helpers.parse_weekday(input_data)
        self.assertEqual(day, "tue")

    def test_parse_weekday_with_empty_string_raises_exception(self):
        input_data = " "
        with self.assertRaises(AttributeError) as err:
            helpers.parse_weekday(input_data)

        # Assert that it informs that the input date is not valid.
        self.assertEqual(str(err.exception),
                         "Cannot parse the date. Is the day in the input date correct?")


if __name__ == "__main__":
    unittest.main()
