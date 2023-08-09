#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    alp = chr(i)

    if i not in ['q', 'e']:
        print('{}'.format(alp), end="")
