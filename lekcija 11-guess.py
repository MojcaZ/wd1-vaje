import random
import json
import datetime

current_time = datetime.datetime.now()
print(current_time)

secret = random.randint(1, 30)
attempts = 0

#v jsonu lahko shranjujemo tudi liste
with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    #score_list.sort()  listo sortiramo
    #print("Najboljši rezultat: " + str(score_list[0]) + ".") #pokažemo samo najboljši rezultat
for score_dict in score_list:
    print(str(score_dict["attempts"]) + " poskusov na datum " +  score_dict.get("date"))

while True:
    guess = int(input("Ugani številko med 1 in 30.\n"))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())}) #zapišemo število poskusov v listo

        with open("score_list.json", "w") as score_file: #shranimo listo v json file
            score_file.write(json.dumps(score_list))

        print("Bravo, uganil_a si. Številka je " + str(secret) + ".")
        print("Potreboval_a si " + str(attempts) + " poskusov.")
        break
    elif guess > secret:
        print("Poskusi z manjšo številko.")
    else:
        print("Poskusi z večjo številko.")
