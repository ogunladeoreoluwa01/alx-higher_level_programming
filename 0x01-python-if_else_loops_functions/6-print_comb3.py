#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if j <= i:
            continue
        if i == 8 and j == 9:
            print("{}{}".format(i, j), end="\n")
        else:
            print("{}{}".format(i, j), end=", ")
