#!/usr/bin/python3
"""JSON writing function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object using JSON representation"""

    with open(filename, "w") as a:
        json.dump(my_obj, a)
