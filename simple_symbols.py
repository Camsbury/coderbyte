def SimpleSymbols(string): 
    if string[0].isalpha() or string[-1].isalpha():
        return False
    for i in range(1,len(string)-1):
        if string[i].isalpha():
            if string[i-1] != '+':
                return False
            if string[i+1] != '+':
                return False
    return True
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SimpleSymbols(raw_input())  
