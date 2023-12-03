"""
Task 2 of the Advent of Code Challenge 2023
Explores the analysis of given text data.
"""

import os
import aoc_config as cfg
import re

ROOTDIR = os.path.join(cfg.PRJDIR, 'solutions_2023')
DATDIR = os.path.join(ROOTDIR, 'data_2023')
DATAPATH = os.path.join(DATDIR, 'data_task_2')
DATAPATHTEST = os.path.join(DATDIR, 'data_task_2_test')


# PART ONE

def task_2_q1(path, red_max, green_max, blue_max):
    """
    Takes the IDs of all the games which satisfied the maximum threshold for every colour.
    Then sums all the respective IDs together.
    """

    id_list = []
    with open(path) as data_obj:
        contents = data_obj.read().splitlines()

        for line in contents:
            split_string = line.replace(':', ',')
            split_string = split_string.replace(';', ',')
            split_string = split_string.split(',')

            counter = 0
            red_list = [int(re.sub(r'(\D+)', "", x)) for x in split_string if 'red' in x]
            if max(red_list) > red_max:
                counter += 1

            green_list = [int(re.sub(r'(\D+)', "", x)) for x in split_string if 'green' in x]
            if max(green_list) > green_max:
                counter += 1

            blue_list = [int(re.sub(r'(\D+)', "", x)) for x in split_string if 'blue' in x]
            if max(blue_list) > blue_max:
                counter += 1

            if counter == 0:
                id_list.append(int(re.sub(r'(\D+)', "", split_string[0])))

    return sum(id_list)


# OUTPUT ANSWER FOR TASK 2 Q1
print(task_2_q1(DATAPATH, 12, 13, 14))


# PART TWO

def task_2_q2(path):
    """
    Calculates the product of all the minimum number of cubes of each colour, for each game.
    Then sums the respective products of each game together.
    """

    power_cubes = []
    with open(path) as data_obj:
        contents = data_obj.read().splitlines()

        for line in contents:
            split_string = line.replace(':', ',')
            split_string = split_string.replace(';', ',')
            split_string = split_string.split(',')

            red_list = [int(re.sub(r'(\D+)', "", x)) for x in split_string if 'red' in x]

            green_list = [int(re.sub(r'(\D+)', "", x)) for x in split_string if 'green' in x]

            blue_list = [int(re.sub(r'(\D+)', "", x)) for x in split_string if 'blue' in x]

            power = max(red_list) * max(green_list) * max(blue_list)
            power_cubes.append(power)

    return sum(power_cubes)


# OUTPUT ANSWER FOR TASK 2 Q1
print(task_2_q2(DATAPATH))


