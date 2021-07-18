
secret = 34

guess = int(input("Guess a number between 1 and 50. \n"))

if guess == secret:
    print("Good job, you guessed it.")
else:
    print("Sorry, you are wrong. The secret number is not " + str(guess) + ".")