#!/usr/bin/python3
"""Defines a from_json_string function."""
import json


def from_json_string(my_str):
    """Return an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        The Python data structure represented by my_str.
    """
    return json.loads(my_str)
