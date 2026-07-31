#!/usr/bin/python3
"""Defines an append_write function."""


def append_write(filename="", text=""):
    """Append text to the end of a UTF8 file, creating it if needed.

    Args:
        filename (str): The path of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
