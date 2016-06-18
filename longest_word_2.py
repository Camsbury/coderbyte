def LongestWord(sen):
    words = word_splitter(sen)
    length = 0
    lword = ""
    for word in words:
        if len(word) > length:
            lword = word
            length = len(word)
    return lword
    
def word_splitter(sen):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    start = 0
    word_flag = False
    words = []
    sen_list = list(sen+"!")
    for index, letter in enumerate(sen_list):
        if (letter in alphabet) and (word_flag == False):
            start = index
            word_flag = True
        elif (letter not in alphabet) and (word_flag == True):
            words.append(sen[start:index])
            word_flag = False
    return words
  
print LongestWord(raw_input())