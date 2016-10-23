def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    n = HAND_SIZE
    iter = 0

    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end the game: ')

        if cmd == 'n':
           hand = dealHand(n)
           iter = 1
           while True:
               playCmd = raw_input('Enter u for the user to play the hand, or c for the computer to play the hand: ')
               if playCmd == 'u':
                   playHand(hand.copy(), wordList, n)
                   break
               elif playCmd == 'c':
                   comPlayHand(hand.copy(), wordList)
                   break
               else:
                   print ("Invalid command.")
           
        elif cmd == 'r':
                if iter == 0:
                    print 'You have not played a hand yet. Please play a new hand first!'
                else:
                    while True:
                        playCmd = raw_input('Enter u for the user to play the hand, or c for the computer to play the hand: ')
                        if playCmd == 'u':
                            playHand(hand.copy(), wordList, n)
                            break
                        elif playCmd == 'c':
                            compPlayHand(hand.copy(), wordList)
                            break
                        else:
                            print "Invalid command."

            elif cmd == 'e':
                return
                break
            else:
                print "Invalid command." 