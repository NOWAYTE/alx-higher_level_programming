#!/usr/bin/python3
""" Read a JSON file"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""

    with open(filename)as a:
        return json.load(a)
