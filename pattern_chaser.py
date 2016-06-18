# -*- coding: utf-8 -*-
"""
Using the Python language, have the function PatternChaser(str)
take str which will be a string and return the longest pattern
within the string. A pattern for this challenge will be defined as:
if at least 2 or more adjacent characters within the string repeat
at least twice. So for example "aabecaa" contains the pattern aa,
on the other hand "abbbaac" doesn't contain any pattern. Your program
should return yes/no pattern/null. So if str were "aabejiabkfabed" the
output should be yes abe. If str were "123224" the output should return
no null. The string may either contain all characters (a through z only),
integers, or both. But the parameter will always be a string type.
The maximum length for the string being passed in will be 20 characters.
If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa".
You must always return the longest pattern possible.

Input:"da2kr32a2"
Output:"yes a2"

Input:"sskfssbbb9bbb"
Output:"yes bbb"
"""

def PatternChaser(string):
    p = ""
    hash = {}
    for i in range(2,len(string)//2+1):
        for j in range(len(string)-i+1):
            if j == 0:
                pat_prev = ""
            else:
                pat_prev = string[j-1:i+j-1]
            pat = string[j:i+j]
            if pat in hash:
                if pat != pat_prev:
                    p = pat
            else:
                hash[pat] = pat
    if p == "":
        return "no null"
    else:
        return "yes " + p