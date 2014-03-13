def isWordGuessed(secretWord, lettersGuessed):
    #result = True
    guessed = ''
    for i in secretWord:
        if i in lettersGuessed:
            #inList = True
            guessed = guessed + i
        else:
            #inList = False
            guessed = guessed + '_ '
        #result = result and inList
        #print i,result
    return guessed
S1='apple'
L1=['a', 'e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(S1,L1)        