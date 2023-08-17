#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n = len(argv)

    for i in range(n):
        print('{}: {}'.format(i, argv[1]))
