"""
Task 1 of the Advent of Code Challenge 2023
Explores the extraction of specific components from text data.
"""

import os
import aoc_config as cfg
import re

ROOTDIR = os.path.join(cfg.PRJDIR, 'solutions_2023')
DATDIR = os.path.join(ROOTDIR, 'data_2023')
DATAPATH = os.path.join(DATDIR, 'data_task_1')
DATAPATHTEST = os.path.join(DATDIR, 'data_task_1_test')


# Part ONE

def task_1_q1(dir):
    """
    Takes the first and last digit from each line in the data and concatenates them into a number.
    Then sums all the generated numbers together.
    """
    number_list = []
    with open(dir) as data_obj:
        contents = data_obj.read().splitlines()
        for line in contents:
            numbers = re.findall(r'\d', line)
            first_last = int(numbers[0] + numbers[-1])
            number_list.append(first_last)

    sum_numbers = sum(number_list)
    return sum_numbers


# OUTPUT ANSWER FOR TASK 1 Q1
print(task_1_q1(DATAPATH))


# Part TWO

def task_1_q2(dir):
    """
    Takes the first and last number considering either digit or text form from each line in the data and concatenates
    them into a number.
    Then sums all the generated numbers together.
    """
    number_list = []
    with open(dir) as data_obj:
        contents = data_obj.read().splitlines()
        for line in contents:
            numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
            for n in range(len(numbers)):
                if numbers[n] == 'one':
                    numbers[n] = '1'
                elif numbers[n] == 'two':
                    numbers[n] = '2'
                elif numbers[n] == 'three':
                    numbers[n] = '3'
                elif numbers[n] == 'four':
                    numbers[n] = '4'
                elif numbers[n] == 'five':
                    numbers[n] = '5'
                elif numbers[n] == 'six':
                    numbers[n] = '6'
                elif numbers[n] == 'seven':
                    numbers[n] = '7'
                elif numbers[n] == 'eight':
                    numbers[n] = '8'
                elif numbers[n] == 'nine':
                    numbers[n] = '9'

            first_last = int(numbers[0] + numbers[-1])
            number_list.append(first_last)

    sum_numbers = sum(number_list)

    return sum_numbers


# OUTPUT ANSWER FOR TASK 1 Q2
print(task_1_q2(DATAPATH))

