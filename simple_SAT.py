# -*- coding: utf-8 -*-
"""
Have the function SimpleSAT(str) read str
str -letters, parenthesis,logical operators and tilde's
representing a Boolean formula.

For example: str may be "(a&b)|c"
which means (a AND b) OR c. Your program should output the string yes if
there is some arrangement of replacing the letters with TRUE or FALSE in
such a way that the formula equates to TRUE. If there is no possible way
of assigning TRUE or FALSE to the letters, then your program should output
the string no. 

n the example above, your program would return yes because
a=TRUE, b=TRUE and c=FALSE would make the formula TRUE.

Another example:
if str is "((a&c)&~a)" which means ((a AND c) AND NOT a) then your program
should output no because it is not possible to assign TRUE or FALSE values
to the letters to produce a TRUE output. 

Input:"(a&b&c)|~a"
Output:yes

Input:"a&(b|c)&~b&~c"
Output:no
"""
from copy import deepcopy

def SimpleSAT(string):
    list_string = list(string)
    alpha_hash = frozenset(x for x in list_string if x.isalpha())
    for item in range(len(list_string)):
        if list_string[item] == "&":
            list_string[item] = " and "
        if list_string[item] == "|":
            list_string[item] = " or "
        if list_string[item] == "~":
            list_string[item] = " not "
    pos = [list_string]
    for alpha in alpha_hash:
        pos1 = deepcopy(pos)
        pos2 = deepcopy(pos)
        for i in range(len(pos)):
            for j in range(len(pos[i])):
                if pos[i][j] == alpha:
                    pos1[i][j] = "True"
                    pos2[i][j] = "False"
        pos = pos1 + pos2
    
    pos = tuple("".join(x) for x in pos)
    for cond in pos:
        if eval(cond) == True:
            return "yes"
    return "no"
    
        