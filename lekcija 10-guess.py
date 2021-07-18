import random

secret = random.randint(1, 30)
attempts = 0

with open("score.txt", "r") as score_file: #odpre in prebere file
    best_score = int(score_file.read())    #shrani vsebino v variablo
    print("Najboljši rezultat: " + str(best_score) + ".")

while True:
    guess = int(input("Ugani številko med 1 in 30. \n"))
    attempts += 1

    if guess == secret:
        if attempts < best_score: # rezultat zapiše samo, če je je porabil manj poskusov kot je trenutni best score
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts)) #zapišemo število poskusov v file
        print("Bravo, uganil_a si. Številka je " + str(secret) + ".")
        print("Potreboval_a si " + str(attempts) + " poskusov.")
        break   #če uganemo, se program konča in izpiše število poskusov
    elif guess > secret:
        print("Poskusi z manjšo številko.")
    else:
        print("Poskusi z večjo številko.")