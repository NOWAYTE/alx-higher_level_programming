#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """A function that adds two tuples"""
    x = tuple_a + (0, 0)
    y = tuple_b + (0, 0)
    """Concatenation ensures both the tuples have atleast two"""

    return (x[0] + y[0], x[1] + y[1])
