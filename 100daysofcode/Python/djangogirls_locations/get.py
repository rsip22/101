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

    cities_list = website.data['location']
    print('Cities file:', cities_list)

    with open(cities_list, 'w') as file:
        new = 'Locations: ' + str(locations)
        file.write(new)


"""
def create_json(data_source, file_name):
    
    Saves JSON to local machine with the info
    
    path_to_file = sys.path[0] + '/' + file_name
    row = json.loads(result.stdout.decode('utf-8'))['rows']
    print(json.dumps(row, indent=2))

    try:
        new_json = open(path_to_file, 'w')
        json.dump(row, data_source)
        new_json.close()
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
"""

create_txt()
