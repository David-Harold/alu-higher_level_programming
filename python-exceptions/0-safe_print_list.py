#!/usr/bin/python3
"""Prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Print up to x elements of my_list on one line.

    Returns the actual number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
