
"""
Find the power set of a given input array
"""

def power_set(arr):
    
    l_arr = len(arr)
    
    if l_arr != len(set(arr)):
        print("Please pass in a set.")
    
    p_set = []
    total = int("1"*l_arr,2)
    
    for i in range(total+1):
        
        mask = "{0:b}".format(i)
        
        while len(mask) < l_arr:
            mask = "0" + mask
            
        temp_set = []
        
        for i in range(l_arr):
            if mask[i] == '1':
                temp_set.append(arr[i])
        
        p_set.append(temp_set)
        
    return p_set
            
        