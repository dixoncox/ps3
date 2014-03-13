def isWordGuessed(secretWord, lettersGuessed):
    result = True
    for i in secretWord:
        if i in lettersGuessed:
            inList = True
        else:
            inList = False
        result = result and inList
        print i,result
    return result
S1='carrot'
L1=['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't']
print isWordGuessed(S1,L1)        