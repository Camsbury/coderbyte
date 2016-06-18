def LetterChanges(string):
    a_low='abcdefghijklmnopqrstuvwxyz'
    a_cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vow='aeiou'
    str_list = list(string)
    for i,l in enumerate(str_list):
        if l == 'z':
            str_list[i] = 'A'
        elif l == 'Z':
            str_list[i] = 'A'
        elif l in a_low:
            str_list[i] = a_low[a_low.find(l)+1]
            if str_list[i] in vow: str_list[i] = str_list[i].upper()
        elif l in a_cap:
            str_list[i] = a_cap[a_cap.find(l)+1]
    return ''.join(str_list)
    
    
#%%
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterChanges(raw_input())