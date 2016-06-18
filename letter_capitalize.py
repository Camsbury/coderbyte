def LetterCapitalize(str):         
    return ' '.join([x.capitalize() for x in str.split(' ')])    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterCapitalize(raw_input())  
