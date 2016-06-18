# -*- coding: utf-8 -*-
"""
Using the Python language, have the function SquareFigures(num)
read num which will be an integer. Your program should return
the smallest integer that when squared has a length equal to num.
For example: if num is 6 then your program should output 317
because 317^2 = 100489 while 316^2 = 99856
which does not have a length of six.

Input:2
Output:4

Input:1
Output:0
"""

from math import ceil

def SquareFigures(num):
    
    if num == 1:
        return 0
        
    num = int("1"+"0"*(num-1))
    
    return int(ceil(num**0.5))