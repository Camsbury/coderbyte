# -*- coding: utf-8 -*-
"""
Using the Python language, have the function KUniqueCharacters(str)
take the str parameter being passed and find the longest substring
that contains k unique characters, where k will be the first character
from the string. The substring will start from the second position
in the string because the first character will be the integer k.
For example: if str is "2aabbacbaa" there are several substrings
that all contain 2 unique characters, namely: ["aabba", "ac", "cb", "ba"],
but your program should return "aabba" because it is the longest substring.
If there are multiple longest substrings, then return the first substring
encountered with the longest length. k will range from 1 to 6. 

Input:"3aabacbebebe"
Output:"cbebebe"

Input:"2aabbcbbbadef"
Output:"bbcbbb"
"""

def KUniqueCharacters(string):
    k = int(string[0])
    temp_word = word = string[1:k+1]
    word_end = k
    while word_end < len(string) - 1:
        if len(set(temp_word)) <= k:
            if len(temp_word) > len(word):
                word = temp_word
            word_end += 1
            temp_word = temp_word + string[word_end]
        else:
            temp_word = temp_word[1:len(temp_word)]
    if len(temp_word) > len(word):
        word = temp_word
    return word
        
    
    