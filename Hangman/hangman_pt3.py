def getAvailableLetters(lettersGuessed):
    '''

    :param lettersGuessed: a list (which letters have been guessed so far)
    :return: this returns a string, made up of letters which reperesent the letters that have not yet been guessed.
    '''

    allletters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    allletters2= allletters[:]

    def duplicateRemoval(R1, R2):
        R1Start = R1[:]
        for x in R1:
            if x in R1Start:
                R2.remove(x)
        return ''.join(str(x) for x in R2)
    return duplicateRemoval(lettersGuessed, allletters2)
