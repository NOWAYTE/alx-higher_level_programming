#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1

    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
