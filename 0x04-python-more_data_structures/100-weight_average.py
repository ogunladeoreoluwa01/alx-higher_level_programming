#!/usr/bin/python3
def weight_average(my_list=[]):
    x = 0
    y = 0
    if my_list == []:
        return 0
    for mem in my_list:
        x += (mem[0] * mem[1])
        y += mem[1]
    return (x / (y))
