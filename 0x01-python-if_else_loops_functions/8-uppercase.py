#!/usr/bin/python3
def uppercase(s):
    for i in s:
        if 'a' <= s <= 'z':
            i = chr(ord(i) - 32)
        print('{}'.format(s), end="")
    print()
