#!/usr/bin/env python

# -*- coding: UTF-8 -*-

"""
Module to provide stock price on opening and closure, on a given range of dates.
Author: rsip22
"""

from urllib.request import urlopen
import datetime
import json
import re


def get_data_from_API(key, value):

    """ Query the API"""

    url = 'https://jsonmock.hackerrank.com/api/stocks/'
    search = f'search?{key}={value}'
    fhand = urlopen(url+search)
    info = json.load(fhand)

    return info


def reformat_date(date):

    """
    Reformat a string into a datetime object in format '%d-%B-%Y',
    even if day is not a zero-padded number.
    Args:
        date: string to represent the date '%d-%B-%Y'
    """

    day, month, year = date.split('-')
    day_numbers = re.compile(r'\d+')
    day = day_numbers.findall(day)[0]
    return datetime.datetime.strptime(f'{day}-{month}-{year}', '%d-%B-%Y')


def open_and_close_prices(first_date, last_date, week_day):
    """
    Get the open and close prices for stocks in a given interval of days.
        args:
            first_date: first date to query, date string in the format %d-%B-%Y
            last_date: last date to query, date string in the format %d-%B-%Y
            week_day: which weekday should be considered, date string in the format %A
    """
    stocks = list()

    # Information available from Monday to Friday
    if week_day == 'Saturday' or week_day == 'Sunday':
        return

    else:
        # Convert to datetime objects
        date_first_date = reformat_date(first_date)
        date_last_date = reformat_date(last_date)
        api_first_date = reformat_date('5-January-2000')
        api_last_date = reformat_date('1-January-2014')

        # Skips processing if date is out of range
        if date_first_date < api_first_date:
            date_first_date = api_first_date
        if date_last_date > api_last_date:
            date_last_date = api_last_date

        dates_to_query = []
        date_to_query = date_first_date

        while date_to_query < date_last_date:
            day = date_to_query.strftime('%A')
            if week_day == day:
                dates_to_query.append(date_to_query.strftime('%d-%B-%Y'))
            date_to_query = date_to_query + datetime.timedelta(days=1)

        for date in dates_to_query:
            # handles days starting with '0', which must be queried as so:
            if date.startswith('0'):
                date = date[1:]
            # Query the API
            key = 'date'
            value = date
            fhand = get_data_from_API(key, value)
            try:
                stock_data = {
                    "date": date,
                    "open": fhand['data'][0]['open'],
                    "close": fhand['data'][0]['close']
                }
                stocks.append(stock_data)
            except IndexError:
                continue
    return stocks


if __name__ == '__main__':
    stock_info = open_and_close_prices('17-January-2000', '22-February-2000', 'Monday')
    for stock in stock_info:
        print(stock['date'])
        print(stock['open'])
        print(stock['close'])
