#!/usr/bin/python3
def uppercase(s):
    for i in s:
        if 'a' <= s <= 'z':
            i = (chr(i) - 32)  
    print('{}'.format(s), end="")
