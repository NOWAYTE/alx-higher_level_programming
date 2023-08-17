#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    argv = sys.argv

    for i in range(len(argv) - 1):
        result += int(argv[i + 1])
    print("{}".format(result))
