def isWordGuessed(secretWord, lettersGuessed):
    """

    :param secretWord: a string (the word the user is guessing)
    :param lettersGuessed: a list, what letters have been guessed so far
    :return: boolean, true if all letters in secretWord are present in lettersGuessed
    """
    count = 0
    for i, c in enumerate(secretWord):
        if c in lettersGuessed:
                count += 1
        if count == len(secretWord):
            return True
        else:
            return False


