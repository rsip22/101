#!/bin/env python3

# Copyright (C) 2018, Renata D'Avila https://rsip22.github.io/blog
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import selenium
import json
import csv
import sys
from selenium import webdriver
import data_source as website


def get_cities():

    """ Get a list of cities from the website """

    driver = webdriver.Firefox()
    driver.get(website.data['url'])

    locations = list()
    count = 0

    try:
        get_city = driver.find_elements_by_class_name("city")
        for item in get_city:
            count = count + 1
            print(count, '-', item.text)
            locations.append(item.text)

        print('total cities:', count)

        driver.close()

        return locations

    except selenium.common.exceptions.NoSuchElementException:
        print('Element not found .')


def create_txt():

    """Save txt to local machine with the info"""

    locations = get_cities()

    file_path = website.data['location'] + '.txt'
    print('Cities file:', file_path)

    with open(file_path, 'w') as file:
        new = 'Locations: ' + str(locations)
        file.write(new)


def create_csv():
    """Save csv to local machine with the info"""

    locations = get_cities()

    file_path = website.data['location'] + '.csv'

    print('Cities file:', file_path)

    with open(file_path, 'w') as file:
        write_location = csv.writer(file, dialect='excel')
        write_location.writerow(locations)


def create_json():
    """Save JSON to local machine (current directory) with the info """

    # file_path = website.data['location'] + '.json'
    file_path = sys.path[0] + '/' + website.data['file_name'] + '.json'

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(get_cities(), json_file, ensure_ascii=False, indent=1)

    print('JSON file path:', file_path)


# create_txt()
# create_csv()
create_json()
