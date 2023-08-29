#!/usr/bin/python3
def safe_print_integer(value):
    try:
        v = '{:d}'.format(value)
        print(v)
        return True
    except (TypeError, ValueError):
        return False
