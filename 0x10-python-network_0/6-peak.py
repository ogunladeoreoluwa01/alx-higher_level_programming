#!/usr/bin/python3
"""This module finds the peak in a list of integers"""


def find_peak(list_of_integers):
    """This algorithm finds the peak of a list"""
    if list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        return list_of_integers[1]
    mid = int((len(list_of_integers)) / 2)
#    #print(f"mid index of {list_of_integers} = {mid}")
    if list_of_integers[mid] > list_of_integers[mid - 1]:
        if ((mid == len(list_of_integers) - 1) or
                (list_of_integers[mid] > list_of_integers[mid + 1])):
            return list_of_integers[mid]
        else:
            mark = mid + 1
            return find_peak(list_of_integers[mid:])
    else:
        return find_peak(list_of_integers[::mid + 1])
