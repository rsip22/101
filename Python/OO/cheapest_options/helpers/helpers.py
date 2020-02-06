import re

from datetime import datetime


def calculate_price_per_category(category, dates):
    # type: (list[dict], (list[tuple])) -> int
    """ Calculate the total price of reservation, summing total weekday with total weekend prices.

    :param category: object which contains weekday_price and weekend_price
    :param dates: object which contains the weekday_count and weekend_count for the dates
    :return: the sum of the prices
    """
    weekdays_total = category.weekday_price * dates.weekday_count
    weekends_total = category.weekend_price * dates.weekend_count
    return weekdays_total + weekends_total


def count_weekend_days(dates_list):
    # type: (list[tuple]) -> int
    """Count the number of weekend days in a list of dates.

    :param dates_list: a list of datetime objects with the dates
    :return: the number of weekend days
    """
    weekend_days = list(filter(lambda x: x.isoweekday() == 6 or x.isoweekday() == 7, dates_list))
    return len(weekend_days)


def parse_date(date_str):
    # type: (str) -> tuple
    """Transform a valid DAYmonthYEAR string into a tuple.

    :param date_str: a full date string with weekday with two or three letters,
                     such as "16Mar2009(mon)" or "17Mar2009(tues).
    :return: Tuple with strings for day, month, year.
    """
    date_input = re.compile(r"(?P<day>\b[\d]{2})(?P<month>[a-zA-Z]{3})(?P<year>[\d]{4})")

    try:
        day, month, year = date_input.search(date_str).groups()
    except AttributeError:
        raise AttributeError("Cannot parse the date. Is the input date correct?")

    return day, month, year


def parse_dates(dates_list):
    # type: (list[str]) -> (list[tuple])
    """Transform a list of dates into a list of datetime dates objects.

    Args:
        dates_list: a list of strings with the dates in the format %d%b%Y and weekday
                    with two or three letters, such as "16Mar2009(mon)" or "17Mar2009(tues).
    Return: list with datetime objects.
    """
    if not dates_list:
        raise ValueError("Dates list cannot be empty. Is the input data correct?")

    dates = []
    for date in dates_list:
        weekday = parse_weekday(date)
        day, month, year = parse_date(date)

        try:
            datetime_date = datetime.strptime(f"{day}{month}{year}({weekday})", "%d%b%Y(%a)")

            dates.append(datetime_date)
        except ValueError:
            raise

    return dates


def parse_weekday(weekday_str):
    # type: (str) -> str
    """Transform the weekday_str into a valid string for weekday.

    Args:
        weekday_str: a full date string with weekday with two or three letters,
                     such as "16Mar2009(mon)" or "17Mar2009(tues).
    Returns:
        A three letter string
    """
    weekday = re.compile(r"(?P<day>[a-z]{3})")
    try:
        weekday_string = weekday.search(weekday_str).group("day")
    except AttributeError:
        raise AttributeError("Cannot parse the date. Is the day in the input date correct?")
    return weekday_string


def parse_string(input_data, delimiter):
    # type: (str, str) -> list[str]
    """Split the input_data string using the delimiter and remove whitespace.

    Args:
        input_data: string to be parsed
        delimiter: to split the string
    Return: list
    """
    if delimiter not in input_data:
        raise SyntaxError("Cannot parse the input. Is it in the correct format?")
    return [item.strip() for item in input_data.split(delimiter)]
