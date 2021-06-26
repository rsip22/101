"""
Module to convert an array of dates into ISO format.
Author: rsip22

"""

import datetime
import re


def reformat_date(dates):
    """
    Converts an array of dates to ISO format.
    Ex: '26th Dec 2061' to '2061-12-26'.
    args:
        dates: array of dates in the format %d-%b-%Y
    """

    reformated_dates = []

    for item in dates:
        day, month, year = item.split(' ')
        day_numbers = re.compile(r'\d+')
        day = day_numbers.findall(day)[0]
        formatted_date = datetime.datetime.strptime(f'{year}-{month}-{day}',
                                                    '%Y-%b-%d')
        reformated_dates.append(
            datetime.date(formatted_date.year,
                          formatted_date.month,
                          formatted_date.day).isoformat())

    return reformated_dates


print(reformat_date(['25th May 1912', '16th Dec 2018', '26th Dec 2061']))
