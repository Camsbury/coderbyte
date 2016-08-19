# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 09:46:15 2016

@author: buddha
"""

def BinarySearchTreeLCA(strArr): 
    traversal = [int(num) for num in strArr[0][1:-1].split(',')]
    nodes = [int(num) for num in strArr[1:]]
    node_paths = []
    for node in nodes:
        node_paths.append(find_node(traversal, node))
    print(node_paths)
    while node_paths[0] and node_paths[1]:
        if node_paths[0][-1] != node_paths[1][-1]:
            break
        common = node_paths[0][-1]
        node_paths[0].pop()
        node_paths[1].pop()
    return common
    
def find_node(traversal, node):
    count = 1
    last = traversal[0]
    path = [last]
    while node != last:
        new = traversal[count]
        if new > last and node > last:
            last = new
            path.append(last)
        elif new < last and node < last:
            last = new
            path.append(last)
        count += 1
    return list(reversed(path))