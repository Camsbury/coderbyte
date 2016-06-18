import re

def LongestWord(sen):
    length = 0
    sen = re.split('\W',sen)
    print(sen)
    for word in sen:
        if len(word) > length:
            lword = word
            length = len(word)
    return lword 
  
print LongestWord(raw_input())