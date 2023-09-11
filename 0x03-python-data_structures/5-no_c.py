#!/usr/bin/python3
def no_c(my_string):
    li = []
    ens = ""
    for i in range(len(my_string)):
        if my_string[i] == "C" or my_string[i] == "c":
            pass
        else:
            li.append(my_string[i])
    return "".join(li)
