# -*- coding: utf-8 -*-
"""
Have the function PermutationStep(num) take the num
parameter being passed and return the next number
greater than num using the same digits. For example:
if num is 123 return 132, if it's 12453 return 12534.
If a number has no greater permutations, return -1 (ie. 999). 

Input:11121
Output:11211

Input:41352
Output:41523
"""

def PermutationsStep(num):
    
    string = str(num)
    if len(string) == 1:
        return -1
    for i in range(len(string)-2,-1,-1):
        if string[i] < string[i+1]:
            return int(string[:i] + string[i+1:] + string[i])
    else:
        return -1