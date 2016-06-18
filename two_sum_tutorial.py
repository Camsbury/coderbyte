# -*- coding: utf-8 -*-
"""
two - sum problem
"""

def two_sum(arr,s):
    
    ans = []
    hash_table = {}
    
    for i in arr:
        
        dif = s - i
        
        if dif in hash_table:
            ans.append((i,dif))
            
        hash_table[i] = i
        
    return ans