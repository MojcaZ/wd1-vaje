import random

cities_dict = {"Austria": "Vienna", "Portugal": "Lisbon", "Germany": "Berlin", "Spain": "Madrid", "UK": "London", "Italy": "Rome", "France": "Paris", "Hungary": "Budapest", "Slovakia": "Bratislava"}

def game():
    country = random.choice(list(cities_dict.keys()))
    guess = input("What is the capital of " + str(country) + "?\n").title()
    if cities_dict[country] == guess:
        print("Good job.")
    else:
        print("Wrong. The correct answer is " + str(cities_dict[country]) + ".")

game()