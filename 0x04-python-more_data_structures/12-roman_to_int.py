#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    temp = 0
    flag = True
    try:
        r = len(roman_string) - 1
        for i in range(r, -1, -1):
            if flag:
                temp += values[roman_string[i]]
            else:
                temp -= values[roman_string[i]]
            if values[roman_string[i - 1]] < values[roman_string[i]]:
                flag = False
            else:
                flag = True
        return temp
    except KeyError:
        return 0
    except TypeError:
        return 0
