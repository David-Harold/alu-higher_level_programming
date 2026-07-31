#!/usr/bin/python3
"""Defines a read_file function."""


def read_file(filename=""):
    """Read a UTF8 text file and print its contents to stdout.

    Args:
        filename (str): The path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
