#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    status = []
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            status.append(True)
        else:
            status.append(False)
    return status
