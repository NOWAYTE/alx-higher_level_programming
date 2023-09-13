#!/usr/bin/python3
"""A function that appends a file """


def append_write(filename="", text=""):
    """Appends a string to the end of a string at the end of a text file"""

    with open(filename, "a", encoding="utf-8") as a:
        return f.write(text)
