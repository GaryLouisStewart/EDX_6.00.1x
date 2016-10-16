

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
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print "-----------"

    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 0

    print 'Welcome to the game, Hangman!'
    print ('I am thinking of a word that is ') + intro + (' letters long.')
    print ('------------')

    while mistakesMade < 8:
        if isWordGuessed(secretWord, lettersGuessed):
            return ('Congratulations, you won!')
        print ('You have ') + str(8 - mistakesMade) + (' guesses left.')
        print ('Available letters:') + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter:').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ('Oops! You\'ve already guessed that letter:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ('Good guess:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ('Oops! You\'ve already guessed that letter:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade += 1
                print ('Oops! That letter is not in my word:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
    return ('Sorry, you ran out of guesses. The word was ') + secretWord

hangman():