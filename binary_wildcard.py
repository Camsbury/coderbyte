# -*- coding: utf-8 -*-
"""
binary wildcard combinations
"""

def ans(s):
    ans = [""]
    for i in s:
        if i == "?":
            ans = [x + "0" for x in ans] + [x + "1" for x in ans]
        else:
            ans = [x + i for x in ans]
    return ans