#!/usr/bin/python3
"""Adds arguments to python list and then save to a file"""

import sys


if __name__ == "__main__":
    from 5-save_to_json_file import save_to_json_file
    from 6-load_from_json_file import load_from_json_file

    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    for arg in sys.arg[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, "add_item.json")
