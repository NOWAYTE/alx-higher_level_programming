#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    alp = chr(i);

    if not (i == 'q') | (i == 'e'):
        print('{}'.format(alp), end="")
