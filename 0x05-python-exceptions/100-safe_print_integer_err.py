#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        if isinstance(value, int):
            print('{}'.format(value))
            return True
        else:
            return False
    except Exception as a:
        sys.stderr.write('Exception: {}'.format(a)
