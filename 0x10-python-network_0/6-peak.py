#!/usr/bin/python3
"""
function that finds the peak in an unsorted array

"""


def find_peak(list_of_integers):
    """
    returns peak in a unsorted array 

    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    m = int(len(list_of_integers) / 2)

    peak = list_of_integers[m]

    if peak > list_of_integers[m - 1] and peak > list_of_integers[m + 1]:
        return peak

    elif peak < list_of_integers[m - 1]:

        return find_peak(list_of_integers[:m])
    else:

        return find_peak(list_of_integers[m + 1:])
