# -*- coding: utf-8 -*-
"""
arr always has an even amount of ints

Have the function ParallelSums(arr) take the array of integers stored in arr
and determine how they can be split into two even sets of integers each
so that both sets add up to the same number.

If this is impossible return -1. If it's possible to split
the array into two sets, then return a string representation of the first
set followed by the second set with each integer separated by a comma and
both sets sorted in ascending order. The set that goes first is the set
with the smallest first integer. 

For example: if arr is [16, 22, 35, 8, 20, 1, 21, 11]
then your program should output 1,11,20,35,8,16,21,22

Input:1,2,3,4
Output:1,4,2,3

Input:1,2,1,5
Output:-1
"""

import itertools

def ParallelSums(arr):
    
    combs = set(itertools.combinations(arr,len(arr)/2))
    
    for a in combs:
        a_sum = sum(a)
        b = arr[:]
        for i in a:
            b.remove(i)
        b_sum = sum(b)
        if a_sum == b_sum:
            ans = compose(list(a),b)
            return ans
    return -1
    
def compose(a,b):
    a.sort()
    b.sort()
    if a[0] <= b[0]:
        return ','.join(str(x) for x in a + b)
    else:        
        return ','.join(str(x) for x in b + a)