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
from selenium import webdriver
import data_source as website


def get_cities():
    driver = webdriver.Firefox()
    driver.get(website.data['url'])

    cities = list()
    cities = driver.find_elements_by_class_name("overlay")

    try:
        for item in cities:
            print('item', item)
            """
            location = driver.find_element_by_class("city")
            cities.append(location)
            """
        print('Cities: ', cities)

        """
        input.send_keys(website.data['login'])
        driver.find_element_by_id('login-form').submit()
        """

    except selenium.common.exceptions.NoSuchElementException:
        print('Element not found .')

    driver.close()

    """

    cookies = driver.get_cookies()
    django_session = cookies[0]['value']
    new = str('django_session=' + django_session)
    cookie_file = website.data['location']
    print('Cookie file:', cookie_file)

    with open(cookie_file, 'w') as file:
        file.write(new)
    
    """


get_cities()
