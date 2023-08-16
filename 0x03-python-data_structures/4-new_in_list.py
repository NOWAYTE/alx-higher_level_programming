#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        copied = my_list[:]
        return (copied)
    if idx > (len(my_list) - 1):
        copied = my_list[:]
        return (copied)
    copied = my_list[:]
    copied[idx] = element
    return (copied)
