#!/usr/bin/python3
"""Inserts a text into a file """


def append_after(filename="", search_string="", new_string=""):
    text = ""

    with open(filename) as a:
        for t in a:
            text += t
            if search_string in t:
                text += new_string

    with open(filename, "w") as x:
        x.write(text)
