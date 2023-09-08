#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    xsum = 0
    for i in range(1, len(argv)):
        xsum += int(argv[i])
    print(xsum)
