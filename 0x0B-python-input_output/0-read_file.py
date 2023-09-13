#!/usr/bin/python3 
"""A function that reads a text"""


def read_file(filename=""):
    """reads a file and prints it to stdout"""

    with open(filename, encoding="utf-8") as a :
        print(a.read(), end="")
