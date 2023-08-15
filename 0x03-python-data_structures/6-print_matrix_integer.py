#!/usr/bin/python3
def print_matric_integer(matrix=[[]]):
    for i in matrix:
        for n in i:
            print(" ", end="")
            print('{:d}'.format(n), end="")
        print()
