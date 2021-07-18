class Player():
    def __init__(self, name, surname, height_cm, weight_kg):
        self.name = name
        self.surname = surname
        self.height_cm = height_cm
        self.weight_kg = weight_kg

class BasketPlayer(Player):
    def __init__(self, name, surname, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(name=name, surname=surname, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FBPlayer(Player):
    def __init__(self, name, surname, height_cm, weight_kg, goals, y_cards, r_cards):
        super().__init__(name=name, surname=surname, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.y_cards = y_cards
        self.r_cards = r_cards


lebron = BasketPlayer(name="Lebron", surname="James", height_cm=203, weight_kg=113, points=27.2,
                      rebounds=7.4, assists=7.2)

kevin = BasketPlayer(name="Kevin", surname="Durant", height_cm=211, weight_kg=115, points=26.5,
                     rebounds=7, assists=6)

ronaldo = FBPlayer(name="Cristiano", surname="Ronaldo", height_cm=184, weight_kg=79, goals=586,
                   y_cards=95, r_cards=11)

messi = FBPlayer(name="Lionel", surname="Messi", height_cm=170, weight_kg=67, goals=575,
                 y_cards=67, r_cards=0)

print(kevin.__dict__)

name = input("Enter player's name:\n")
surname = input("Enter player's surname:\n")
height_cm = input("Enter player's height in cm:\n")
weight_kg = input("Enter player's weight in kg:\n")

new_player = Player(name=name, surname=surname, height_cm=height_cm, weight_kg=weight_kg)


with open("players.txt", "a") as players_list:
    players_list.write(str(new_player.__dict__))

print("Player added!")
print(new_player.__dict__)