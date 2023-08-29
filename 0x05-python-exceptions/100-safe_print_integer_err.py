#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        if isinstance(value, int):
            print('{:d}'.format(value))
            return True
    except Exception as a:
        sys.stderr.write('Exception: {:d}'.format(a))
        return False
