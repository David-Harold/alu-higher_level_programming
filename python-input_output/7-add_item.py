#!/usr/bin/python3
"""Adds all command line arguments to a list and saves it as JSON."""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        add_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        add_list = []

    add_list.extend(sys.argv[1:])

    save_to_json_file(add_list, "add_item.json")
