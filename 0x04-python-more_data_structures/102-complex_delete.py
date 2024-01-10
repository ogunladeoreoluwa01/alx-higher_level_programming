#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    count = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            count.append(key)
    for mem in count:
        del a_dictionary[mem]
    return a_dictionary
