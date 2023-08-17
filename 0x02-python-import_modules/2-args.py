#!/usr/bin/python3
import sys
count = len(sys.argv) - 1
if __name__ == "__main__":
    for i in range(count):
        print("{}: arguments {}".format(i + 1, sys.argv[i + 1]))
