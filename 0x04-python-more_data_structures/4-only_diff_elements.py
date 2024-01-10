#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1 = [x for x in set_1 if x not in set_2]
    set2 = [x for x in set_2 if x not in set_1]
    return set(set1 + set2)
