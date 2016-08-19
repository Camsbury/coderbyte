# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:48:35 2016

@author: buddha
"""

def BinaryTreeLCA(strArr): 
    traversal = [num for num in strArr[0][1:-1].split(', ')]
    for i, num in enumerate(traversal):
        if num != "#":
            traversal[i] = int(num)
    nodes = [int(num) for num in strArr[1:]]
    node_paths = []
    for node in nodes:
        node_paths.append(find_path(traversal, node))
    common = traversal[0]
    while node_paths[0] and node_paths[1]:
        if node_paths[0][-1] != node_paths[1][-1]:
            break
        common = node_paths[0][-1]
        node_paths[0].pop()
        node_paths[1].pop()
    return common
    
def find_path(traversal, node):
    
    path = [node]
    index = traversal.index(node)
    while index > 0:
        index = (index-1)//2
        path.append(traversal[index])
    
    return path