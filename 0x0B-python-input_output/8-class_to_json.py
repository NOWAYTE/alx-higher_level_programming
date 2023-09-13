#!/usr/bin/python3
"""Class-JSON function"""


def class_to_json(obj):
    """Returns dictionary description with somple data structure"""

    return obj.__dict__
