def FirstFactorial(num):
    if num>1:
        num=num*FirstFactorial(num-1)
    return num
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print FirstFactorial(raw_input())  
