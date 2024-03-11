#!/usr/bin/python3

"""Defines MyInt class"""


class MyInt(int):
    """Represents MyInt class which inherits from int"""

    def __eq__(self, other):

        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
