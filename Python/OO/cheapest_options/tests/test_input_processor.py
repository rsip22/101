import unittest

from models import input_processor


class InputProcessorTestCase(unittest.TestCase):

    """Tests for the Input Processor class."""

    def test_correct_input_line_parses_to_correct_client_type_and_reservation_date(self):
        input_data = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        input_parsed = input_processor.InputProcessor(input_data)

        # Assert that the input is properly split into client_type and reservation_date
        self.assertEqual("Regular", input_parsed.client_type)
        self.assertEqual(["16Mar2009(mon)", "17Mar2009(tues)", "18Mar2009(wed)"],
                         input_parsed.reservation_dates)

    def test_correct_input_client_with_spaces_splits_to_client_type_and_reservation_date(self):
        input_data = " Regular : 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        input_split = input_processor.InputProcessor(input_data)

        # Assert that the input is properly split into client_type and reservation_date
        self.assertEqual("Regular", input_split.client_type)
        self.assertEqual(["16Mar2009(mon)", "17Mar2009(tues)", "18Mar2009(wed)"],
                         input_split.reservation_dates)

    def test_incorrect_client_type_but_correct_reservation_date_throws_error(self):
        input_data = "Revards: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"

        # Assert it throws a ValueError
        with self.assertRaises(ValueError) as err:
            input_processor.InputProcessor(input_data)

        # Assert that it informs that the Client type not valid.
        self.assertEqual(str(err.exception), "Client type is not valid.")

    def test_empty_client_type_but_correct_reservation_date_returns_regular(self):
        input_data = "16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"

        input = input_processor.InputProcessor(input_data)
        self.assertEqual(input.client_type, "regular")

        # # Assert that a SyntaxError is raised instead of splitting the data
        # with self.assertRaises(SyntaxError) as err:
        #     input_processor.InputProcessor(input_data)
        #
        # # Assert that it informs that the date format provided is not valid.
        # self.assertEqual(str(err.exception), "Cannot parse the input. Is it in the correct format?")

    def test_correct_client_type_but_incorrect_str_as_month_on_reservation_date_splits_the_input(self):
        input_data = "Rewards: 16Sat2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        _, input_dates = [item.strip() for item in input_data.split(":")]
        input_parsed = input_processor.InputProcessor(input_data)

        # Assert that the input is properly split into client_type and reservation_date list
        self.assertEqual("Rewards", input_parsed.client_type)
        self.assertEqual(["16Sat2009(mon)", "17Mar2009(tues)", "18Mar2009(wed)"],
                         input_parsed.reservation_dates)

    def test_correct_client_type_but_empty_reservation_date_throws_error(self):
        input_data = "Rewards: "

        # Assert that attempting to split the input will raise a SyntaxError
        with self.assertRaises(SyntaxError) as err:
            input_processor.InputProcessor(input_data)

        # Assert that it informs that the date format provided is not valid.
        self.assertEqual(str(err.exception), "Cannot parse the input. Is it in the correct format?")

    def test_empty_data_throws_error(self):
        input_data = " "

        # Assert that attempting to split the input will raise a SyntaxError
        with self.assertRaises(SyntaxError) as err:
            input_processor.InputProcessor(input_data)

        # Assert that it informs that the date format provided is not valid.
        self.assertEqual(str(err.exception), "Cannot parse the input. Is it in the correct format?")


if __name__ == "__main__":
    unittest.main()
