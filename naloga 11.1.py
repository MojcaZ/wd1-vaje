import random
import json
from datetime import date

current_date = date.today()
date = current_date.strftime("%d. %m. %Y")
secret = random.randint(1, 30)
attempts = 0
name = input("Vnesi svoje ime:\n").title()

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    best_scores = sorted(score_list, key=lambda a: a["attempts"])[:3] #lambda vrne, kar je napisano v oklepajih


for score_dict in best_scores:
    print("{2} je imel_a {0} poskusov na {1}. Skrivna številka je bila {3}, napačni poskusi pa {4}.".format(score_dict.get("attempts"),
                                                                                                              score_dict.get("date"),
                                                                                                              score_dict.get("player_name"),
                                                                                                              score_dict.get("secret_number"),
                                                                                                              score_dict.get("wrong_guesses")))
wrong_guesses = []

guess = int(input("Ugani številko med 1 in 30.\n"))

while True:
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": date, "player_name": name, "secret_number": secret, "wrong_guesses": wrong_guesses})
        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Bravo, uganil_a si. Številka je " + str(secret) + ".")
        print("Potreboval_a si " + str(attempts) + " poskusov.")
        break

    elif guess > secret:
         guess = int(input("Poskusi z manjšo številko.\n"))
    else:
         guess = int(input("Poskusi z večjo številko.\n"))

    wrong_guesses.append(guess)