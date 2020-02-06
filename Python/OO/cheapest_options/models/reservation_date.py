from helpers import helpers


class ReservationDate:
    """
    Class to process the dates for reservations.
    """
    def __init__(self, reservation_dates_list):
        """
        :param reservation_dates_list: a list of strings with the reservation dates. Sample format:
                                       ["16Mar2009(mon)", "17Mar2009(tues)", "18Mar2009(wed)"]
        """
        self.reservation_dates_list = helpers.parse_dates(reservation_dates_list)
        self.length_of_stay = self._get_length_of_stay()
        self.weekend_count = self._get_weekend_count()
        self.weekday_count = self._get_weekday_count()

    def _get_weekend_count(self):
        """Count the weekend days in the reservation."""
        return helpers.count_weekend_days(self.reservation_dates_list)

    def _get_weekday_count(self):
        """Count the number of weekdays in the reservation."""
        return self.length_of_stay - self.weekend_count

    def _get_length_of_stay(self):
        """Count the total of days in the reservation."""
        return len(self.reservation_dates_list)
