#!/usr/bin/python3
"""Inserts a text into a file """


def append_after(filename="", search_string="", new_string=""):
    text = ""

    with open(filename) as a:
        for l in a:
            text += l
            if search_string in l:
                text += new_string

    with open(filename, "w") as x:
        x.write(text)
