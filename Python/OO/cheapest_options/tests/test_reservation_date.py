import unittest

from datetime import datetime

from models import reservation_date


class ReservationDateTestCase(unittest.TestCase):

    """Tests for the Reservation Date class."""

    def test_correct_reservation_dates_list_parses_to_correct_reservation_date_datetime(self):
        input_data = ["16Mar2009(mon)", "17Mar2009(tues)", "18Mar2009(wed)"]
        reservation_dates = reservation_date.ReservationDate(input_data)

        # Assert that the output is properly parsed into datetime objects
        self.assertEqual([datetime(2009, 3, 16, 0, 0),
                          datetime(2009, 3, 17, 0, 0),
                          datetime(2009, 3, 18, 0, 0)], reservation_dates.reservation_dates_list)

    def test_incorrect_str_for_month_on_reservation_date_throws_error(self):
        input_data = ["16Sat2009(mon)", "17Mar2009(tues)", "18Mar2009(wed)"]
        wrong_reservation_date = input_data[0]

        # Assert that attempting to parse it throws a ValueError
        with self.assertRaises(ValueError) as err:
            reservation_date.ReservationDate(input_data)

        # Assert that it informs that the date format provided is not valid.
        self.assertEqual(str(err.exception),
                         f"time data '{wrong_reservation_date}' does not match format '%d%b%Y(%a)'")

    def test_incorrect_year_on_reservation_date_throws_error(self):
        input_data = ["16Sat9999(mon)", "17Mar2009(tues)", "18Mar2009(wed)"]
        wrong_reservation_date = input_data[0]

        # Assert that attempting to parse it throws a ValueError
        with self.assertRaises(ValueError) as err:
            reservation_date.ReservationDate(input_data)

        # Assert that it informs that the date format provided is not valid.
        self.assertEqual(str(err.exception),
                         f"time data '{wrong_reservation_date}' does not match format '%d%b%Y(%a)'")


if __name__ == "__main__":
    unittest.main()
