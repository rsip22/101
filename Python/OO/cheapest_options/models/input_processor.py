from helpers import helpers
from enums import client


class InputProcessor:
    """
    Class for processing the input data, splitting it into: client_type(str)
                                                            reservation_dates list(str).
    """

    def __init__(self, input_data):
        """
        :param input_data: string with the format: <client_type>: <date1>, <date2>, <date3>, …
        """
        if not input_data:
            raise SyntaxError("Input cannot be empty.")

        try:
            client_type, input_dates = helpers.parse_string(input_data, ":")
        except SyntaxError:
            client_type = client.ClientType.REGULAR.value
            input_dates = input_data

        reservation_dates = helpers.parse_string(input_dates, ",")

        if client_type.lower() not in (client.ClientType.REGULAR.value,
                                       client.ClientType.REWARDS.value):
            raise ValueError("Client type is not valid.")

        self.client_type = client_type.strip()
        self.reservation_dates = reservation_dates
