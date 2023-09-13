#!/usr/bin/python3
"""Writes a string """


def write_file(filename="", text=""):
    """write to UTF file"""

    with open(filename, "w", encoding="utf-8") as a:
        return a.write(text)
