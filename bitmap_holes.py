# -*- coding: utf-8 -*-
"""
Using the Python language, have the function BitmapHoles(strArr) 
take the array of strings stored in strArr, which will be a 2D matrix 
of 0 and 1's, and determine how many holes, or contiguous regions of 0's, 
exist in the matrix. A contiguous region is one where there is a 
connected group of 0's going in one or more of four directions: up, 
down, left, or right. For example: if strArr is 
["10111", "10101", "11101", "11111"], then this looks like the following matrix: 
1 0 1 1 1
1 0 1 0 1
1 1 1 0 1
1 1 1 1 1 
For the input above, your program should return 2 because
there are two separate contiguous regions of 0's, which create 
"holes" in the matrix. You can assume the input will not be empty. 

Input:"01111", "01101", "00011", "11110"
Output:3

Input:"1011", "0010"
Output:2
"""

def BitmapHoles(strArr):
    bitmap = {}
    for i in range(len(strArr)):
        for j in range(len(strArr[i])):
            bitmap[(i,j)] = int(strArr[i][j])
    
    hole_count = 0
    hole = set()
    checked = set()
    flag = True
    
    for i in range(len(strArr)):
        for j in range(len(strArr[i])):
            stack = [(i,j)]
            while stack:
                coords = stack.pop()
                if coords not in checked:
                    checked.add(coords)
                    if bitmap[coords] == 0 and coords not in hole:
                        hole.add(coords)
                        if flag == True:
                            hole_count += 1
                            flag = False
                        if coords[0] - 1 >= 0 and (coords[0]-1,coords[1]) not in checked:
                            stack.append((coords[0]-1,coords[1]))
                        if coords[0] + 1 < len(strArr) and (coords[0]+1,coords[1]) not in checked:
                            stack.append((coords[0]+1,coords[1]))
                        if coords[1] - 1 >= 0 and (coords[0],coords[1]-1) not in checked:
                            stack.append((coords[0],coords[1]-1))
                        if coords[1] + 1 < len(strArr[coords[0]]) and (coords[0],coords[1]+1) not in checked:
                            stack.append((coords[0],coords[1]+1))
            flag = True
            
    return hole_count