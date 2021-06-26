#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import copy
import csv

from collections import Counter
from operator import itemgetter

NATIONALITY = set()             # Unique nationalities
CLUBS = set()                   # Unique clubs
PLAYERS_FULL_NAME = list()      # Players full names
PLAYERS_WAGE = list()           # Items: (full_name, eur_wage)
PLAYERS_AGE = list()            # Items: (full_name, age)
AGE_RANGE = list()              # Items: age

# Q3
FIRST_ON_THE_LIST = 20
# Q4, Q5
TOP_PLAYERS = 10


def top_players(players, top_players):
    """
    Find out the top players from a given list.
    Args:
        players: list of tuples containing (player_name, column_to_sort)
        top_players: amount of top players to filter
    """
    players = sorted(players, key=itemgetter(1), reverse=True)[:top_players]
    return [x[0] for x in players]


with open('data.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    for idx, row in enumerate(reader):
        NATIONALITY.add(row['nationality'])
        CLUBS.add(row['club'])
        PLAYERS_WAGE.append((row['full_name'], float(row['eur_wage'])))
        PLAYERS_AGE.append((row['full_name'], int(row['age'])))
        AGE_RANGE.append(int(row['age']))

        if idx < FIRST_ON_THE_LIST:
            PLAYERS_FULL_NAME.append(copy.copy(row['full_name']))

# All questions refer to the file `data.csv`
# You **CANNOT** use Pandas or NumPy to solve this challenge.


# **Q1.** How many unique nationalities (column `nationality`) exist on the file?
def q_1():
    return len(NATIONALITY)


# **Q2.** How many unique clubs (column `club`) exist on the file?
def q_2():
    return len(CLUBS)


# **Q3.** List the full name of the first 20 players on the column  `full_name`.
def q_3():
    return PLAYERS_FULL_NAME


# **Q4.** Who are the top 10 players who made more money (use the columns `full_name` and `eur_wage`)?
def q_4():
    return top_players(PLAYERS_WAGE, TOP_PLAYERS)


# **Q5.** Who are the 10 oldest players?
def q_5():
    return top_players(PLAYERS_AGE, TOP_PLAYERS)


# **Q6.** Count how many players have the same age. To do this, create a dictionary where the keys are the age
# and the values are the counter.
def q_6():
    return Counter(AGE_RANGE)


if __name__ == '__main__':
    print('Q1. How many unique nationalities (column `nationality`) exist on the file?')
    print(q_1())
    print('\nQ2. How many unique clubs (column `club`) exist on the file?')
    print(q_2())
    print('\nQ3. List the full name of the first 20 players on the column  `full_name`.')
    for idx, answer in enumerate(q_3()):
        print(idx + 1, answer)
    print('\nQ4. Who are the top 10 players who made more money (use the columns `full_name` and `eur_wage`)?')
    for idx, answer in enumerate(q_4()):
        print(idx + 1, answer)
    print('\nQ5. Who are the 10 oldest players?')
    for idx, answer in enumerate(q_5()):
        print(idx + 1, answer)
    print('\nQ6. Count how many players have the same age')
    print(q_6())
