# -*- coding: utf-8 -*-
"""
Using the Python language, have the function BipartiteMatching(strArr)
read strArr which will be an array of hyphenated letters representing
paths from the first node to the second node.

For example: ["a->d", "a->e", "b->f", "c->e"] means that
there is a path from node a to d, a to e, b to f, and so on.

The graph will be bipartite meaning that it is possible to separate
the nodes into two disjoint sets such that every edge only connects
a node from the lefthand side to a node on the righthand side.

Your program should determine the maximum cardinality matching
of the bipartite graph, which means finding the largest possible number
of non-adjacent edges that are matching. So for the example above,
your program should return 3 because it is possible to connect
every single node on the left to a node on the right. 

The input will only contain lowercase alphabetic characters with
a -> between them signifying an edge between them going from
the left node to the right node.

The input will contain at least 1 edge connecting 2 nodes. 

Input:"a->w", "a->x", "b->x", "b->y", "c->x", "c->z", "d->w"
Output:4

Input:"a->b", "c->b", "c->d", "e->b"
Output:2
"""

def BipartiteMatching(strArr):
    card = 0
    edges = [tuple(s.split("->")) for s in strArr]
    adjacencies = {}

    for edge1 in edges:
        adjacencies[edge1] = []
        for node in edge1:
            for edge2 in edges:
                if node in edge2:
                    if edge2 != edge1:
                        adjacencies[edge1].append(edge2)
        adjacencies[edge1] = list(set(adjacencies[edge1]))
    
    while edges:
        small_len = float('inf')
        for edge in edges[:]:
            print(adjacencies[edge])
            adj_count = len(adjacencies[edge])
            if adj_count == 0:
                card += 1
                edges.remove(edge)
                if len(edges) == 0:
                    return card
                continue
            if adj_count < small_len:
                smallest = edge
                small_len = adj_count
        kill = adjacencies[smallest][-1]
        for edge in adjacencies[kill]:
            adjacencies[edge].remove(kill)
        edges.remove(kill)
        
    return card