#!/usr/bin/python3
"""A module that contains a function that prints a text"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters
       . ? and :
       Arguments:
            text --text to print 
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in text:
        print(c, end="")

        if c in [".", "?", ":"]:
            print("\n\n", end="")

