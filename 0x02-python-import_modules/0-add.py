#!/usr/bin/python3
from add_0 import add
"""A program that imports a function"""
a = 1
b = 2
if __name__ == "__main__":
    print('{} + {} = {}'.format(a, b, add(a, b)))
