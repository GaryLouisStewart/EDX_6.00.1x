def getGuessedWord(secretWord, lettersGuessed):
    '''

    :param secretWord: string (the word the user is guessing)
    :param lettersGuessed:  list (which letters have been guessed so far?)
    :return: string (madeup of letters and using underscores to represent which letters in secretWord have been
        guessed so far.)
    '''
    count = 0
    gap = ['_ '] * len(secretWord)

    for x, y in enumerate(secretWord):
        if y in lettersGuessed:
            count += 1
            gap.insert(count-1,y)
            gap.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
        else:
            count += 1
            gap.insert(count-1,'_')
            gap.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)