#!/usr/bin/python3
"""Defines a load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Return an object created from a JSON file's content.

    Args:
        filename (str): The path of the JSON file to read.

    Returns:
        The Python data structure represented by the file's content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
