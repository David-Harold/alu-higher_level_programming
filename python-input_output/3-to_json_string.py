#!/usr/bin/python3
"""Defines a to_json_string function."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object.

    Args:
        my_obj: The object to serialize.

    Returns:
        str: The JSON representation of my_obj.
    """
    return json.dumps(my_obj)
