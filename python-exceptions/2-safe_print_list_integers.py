#!/usr/bin/python3
"""Prints the first x elements of a list, integers only."""


def safe_print_list_integers(my_list=[], x=0):
    """Print only the integer elements among the first x of my_list.

    Non-integer elements are skipped silently.
    If x is bigger than the list, an IndexError is allowed to propagate.
    Returns the number of integers actually printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
