#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    v = my_list[0]
    for ma in range(len(my_list)):
        if my_list[ma] >= v:
            v = my_list[ma]
    return v
