secret = 34
guess = int(input("Guess a number between 1 and 50. \n"))
if guess == secret:
    print("Good job, you guessed it.")
else:
    print("Sorry, you are wrong. The secret number is not " + str(guess) + ".")
    # s str(guess) smo številko spremenili v string

#za ugibanje, dokler ne ugane prave številke, imamo while loop:
#ima neskončno število poskusov

secret = 34
guess = 0
while guess != secret:  #tu bi lahko rekli tudi "while True". v tem primeru ne bi rabili definirat guessa
    guess = int(input("Guess a number between 1 and 50."))
    if guess == secret:
        print("Good job, you guessed it.")
        break  #če ugane, se loop prekine
    elif guess > secret:
        print("Wrong. Try a smaller number.")
    else:
        print("Wrong. Try a bigger number.")

#for loop imamo za omejeno število ponovitev

secret = 34
for x in range(5):  #loop se ponovi 5-krat
    guess = int(input("Guess the secret number."))
    if guess == secret:
        print("Good job, you guessed it.")
        break  #če ugane, se loop prekine
    else:
        print("Sorry, you are wrong.")

# importiramo random in naročimo računalniku, naj izbere številko

import random

secret = random.randint(1, 30)

while True:
    guess = int(input("Ugani številko med 1 in 30. "))
    if guess == secret:
        print("Bravo, uganila si. Številka je " + str(secret))
    elif guess > secret:
        print("Poskusi z manjšo številko. ")
    else:
        print("Poskusi z večjo številko. ")