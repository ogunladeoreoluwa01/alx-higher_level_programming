#!/usr/bin/python3
def uniq_add(my_list=[]):
    xsum = 0
    for i in (set(my_list)):
        xsum += i
    return xsum
