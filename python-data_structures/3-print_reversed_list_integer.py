#!/usr/bin/python3
"""Module that prints all integers of a list, in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line."""
    for idx in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[idx]))
