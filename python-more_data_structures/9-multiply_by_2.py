#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        value *= 2
        new_dictionary [key] = value
    return new_dictionary
