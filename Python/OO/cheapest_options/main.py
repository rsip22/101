"""
#!/usr/bin/env python3
.. module:: main
   :synopsis: A program to find the cheapest hotel rate for a given list of dates
   :author: rsip22
"""
import argparse
import locale
import logging

from models import input_processor, price, reservation_date
from enums import client


def setup():
    """Setup the application."""

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    console_out = logging.StreamHandler()
    console_out.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    console_out.setFormatter(formatter)
    log.addHandler(console_out)
    locale.setlocale(locale.LC_ALL, "en_US")


def run(input_line):
    """Run the program.

    :param input_line: string with the format:
                       <client_type>: <date1>, <date2>, <date3>, …
    :output: prints the name of the cheapest hotel for the date
    """

    # Parse the input provided
    parsed_line = input_processor.InputProcessor(input_line)

    # Find the information for the dates
    dates = reservation_date.ReservationDate(parsed_line.reservation_dates)

    # Find the information about the client
    is_rewards = parsed_line.client_type.lower() == client.ClientType.REWARDS.value

    # Instantiate hotel objects for each category
    hotels_from_the_chain = price.Price(dates, is_rewards)

    # Get the cheapest hotel
    cheapest = hotels_from_the_chain.cheapest["name"]
    return cheapest


if __name__ == "__main__":
    setup()
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'), default="samples/sample_data.txt")
    args = arg_parser.parse_args()

    with open(args.input_file.name, "r", encoding="utf-8", errors="strict") as fhand:
        for line in fhand:
            print(run(line))
