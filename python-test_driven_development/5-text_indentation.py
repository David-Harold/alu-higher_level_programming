#!/usr/bin/python3
"""Defines a function that prints text with extra indentation.
"""


def text_indentation(text):
    """Print text, inserting two new lines after each ``.``, ``?`` or ``:``.

    Args:
        text (str): the text to print

    There is no leading or trailing space on any printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special = ".?:"
    line = ""
    for char in text:
        if char == "\n":
            char = " "
        if line == "" and char == " ":
            continue
        line += char
        if char in special:
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
