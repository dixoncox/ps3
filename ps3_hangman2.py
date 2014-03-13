def isWordGuessed(secretWord, lettersGuessed):
    #result = True
    guessed = ''
    for i in secretWord:
        if i in lettersGuessed:
            guessed = guessed + i
        else:
            guessed = guessed + '_ '
    return guessed
S1='apple'
L1=['a', 'e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(S1,L1)        