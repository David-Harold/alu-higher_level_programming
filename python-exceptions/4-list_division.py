#!/usr/bin/python3
"""Divides two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Return a new list of length list_length with element-wise divisions.

    Any element that can't be divided becomes 0, with an explanatory
    message printed: "wrong type", "division by 0", or "out of range".
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
