#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = '{:d}'.formtat(value)
        print(value)
        return True
    except:
        return False
