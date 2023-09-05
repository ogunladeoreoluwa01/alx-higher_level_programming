#!/usr/bin/python3
def remove_char_at(str, n):
    temo = ""
    i = 0
    if len(str) < n or n < 0:
        return str
    temo = str[:n] + str[n + 1:]
    return temo
