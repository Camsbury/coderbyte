# -*- coding: utf-8 -*-
"""
find duplicates in an array with values from 0 to len(array)-1
"""

def get_dups(array):
    ht = {}
    dups = []
    for x in array:
        if x in ht:
            dups.append(x)
        else:
            ht[x] = x
    return list(set(dups))