print ("Please think of a number between 0 and 100!")

high = 100
low = 0
guessed = False

while not guessed:
    guess = (high + low)//2
    print("Is your secret number  " + str(guess)+ "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate the guess is correct.")

    if user_input == 'c':
        guessed = True
    elif user_input == 'h':
        high = guess
    elif user_input == 'l':
        low = guess
    else:
        print("Sorry, I did not understand your input.")
print('Game over. Your secret number was: ' + str(guess))