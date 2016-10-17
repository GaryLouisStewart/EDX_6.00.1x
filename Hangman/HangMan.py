#
# Hangman game
#

#load our list of words into a variable

def isWordGuessed(secretWord, lettersGuessed):
    """

    :param secretWord: a string (the word the user is guessing)
    :param lettersGuessed: a list, what letters have been guessed so far
    :return: boolean, true if all letters in secretWord are present in lettersGuessed
    """
    count = 0
    for x, y in enumerate(secretWord):
        if y in lettersGuessed:
                count += 1
        if count == len(secretWord):
            return True
        else:
            return False


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

def hangman(secretWord):
    '''

    :param secretWord: string, the secret word to guess.

    This will startup an interactive game of hangman.

    * at the start, we will let our user know how many
      letters contains

    * ask our user to try and guess (one letter each round)

    * After our user has guessed they should receive some feedback on
      if their guess has appeared in the computers word

    * at the end of each round the user should get a display of the
      partially guessed word

    '''

    start = str(len(secretWord))
    lettersGuessed = []
    guess = raw_input("\n\nEnter your guess: ")
    incorrectGuesses = 8
    wordGuessed = False


    print 'Welcome to Hangman!'
    print (' I am thinking of a word that is ') + start + (' letters long. )
    print ('------------')

    while incorrectGuesses > 0 and incorrectGuesses <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ('you have ') + str(mistakesMade) + (' guesses left.')
        print ('Available letters: ') + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ("Oops! you've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ('Good Guess: ') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ("Oops! you have already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')

            else:
                lettersGuessed.append(guess)
                incorrectGuesses -= 1
                print ('Oops! that letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')

    if wordGuessed == True:
        return 'Congratulations, you won!'
    elif incorrectGuesses == 0:
        print ('Sorry, you ran out of guesses. The word was ') + secretWord

hangman(secretWord=word)