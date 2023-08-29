#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        if isinstance(value, int):
            print('{:d}'.format(value))
            return True
        else:
            raise TypeError("Value not integer")
    except Exception as a:
        sys.stderr.write('Exception: {}'.format(str(a)))
        return False
