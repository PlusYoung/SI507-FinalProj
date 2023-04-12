# -*- coding: utf-8 -*-
# @Author  : Yang Yang
# @UniqueName : yyanga
# @Time    : 2023/4/9 14:49
# @File    : checkInput.py

import functools
import re
import constant


def validate_cache_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_input = func(*args, **kwargs)
        while True:
            if user_input == 'None':
                return 'movie_data.json'
            elif re.match(r'^[\w_-]+\.json$', str(user_input)):
                return user_input
            else:
                user_input = input("The input is not valid. Please enter a valid input [JSON file name or 'None']. "
                                   "'None' means the Json file name is 'movie_data.json'.")

    return wrapper


def validate_start_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_input = func(*args, **kwargs)
        while True:
            set_a = user_input
            if isinstance(args[0], list):
                set_b = set(args[0])
            else:
                set_b = set(str(i) for i in args[0].keys())
            # print(set_b)
            if set_a.issubset(set_b):
                # print(user_input)
                return list(user_input)
            else:
                user_input = set(input(
                    "{} is invalid input! Please check again and input all you need: ".format(set_a - set_b)).split(
                    ' '))

    return wrapper


def validate_choice_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_input = func(*args, **kwargs)
        while True:
            if user_input.isdigit():
                if int(user_input) in [1, 2, 3, 4, 5]:
                    return user_input
                else:
                    user_input = input("Invalid input! Please give your choice from 1 to 5: ")
            else:
                user_input = input("Invalid input! Please give your choice from 1 to 5: ")

    return wrapper


def validate_detail_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_input = func(*args, **kwargs)
        set_a = set(user_input.split(","))
        # print(args[1])
        set_b = set(args[1].keys())
        # print(args[1].keys())
        while True:
            set_a = set(user_input.split(","))
            if set_a.issubset(set_b):
                return user_input.split(",")
            else:
                user_input = input("Some movies you gave are not in our recommendation list! Please check it "
                                   "and provide movie names again [use comma to separate movies] (e.g. "
                                   "Britannic,The Crossing,Vola sciusciù): ")

    return wrapper


@validate_cache_input
def self_input(path):
    return input(path)


@validate_start_input
def start_input(database=None):
    if isinstance(database, dict):
        return set(input(
            "Please enter the corresponding code(s) for your preferred movie genre(s) that our database must covered, "
            "separated by spaces. (e.g. 28 12 16): ").split(' '))
    else:
        return set(input(
            "Please enter the year(s)[2000-2022] of the movie(s) you would like to be recommended, separated by "
            "spaces. (e.g. 2000 2001 2002) :").split(' '))


@validate_choice_input
def choice_input(choice):
    return input(choice)


@validate_detail_input
def detail_input(name, data_recommend):
    return input(name)
