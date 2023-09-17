#!/usr/bin/python3
"""A function that traverses a matrix"""


def traverse_matrix():
    matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    
    for i in matrix:
        for row in i:
            print(row, end=" ")
        print()

traverse_matrix()
