#!/usr/bin/python3
def print_last_digit(number):
    l_digit = abs(number) % 10
    print('{}'.format(number), end=" ")

    return l_digit
