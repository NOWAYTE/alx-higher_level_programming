#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n = len(argv)

    if n == 0:
        print("0 arguments")

    elif n == 1:
        print("1 arguments")

    else:
        print('{} arguments:'.format(n))

    for i in range(n):
        print('{}: {}'.format(i, argv[1]))
