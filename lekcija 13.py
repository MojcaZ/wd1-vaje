class BasketPlayer():  # ime classa
    def __init__(self, name, surname, height_cm, weight_kg, points, rebounds, assists):  # funkcija za ustvarjanje novega objekta
        self.name = name
        self.surname = surname
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def weight_to_lbs(self):  # to je metoda
        pounds = self.weight_kg * 2.204
        return pounds


lebron = BasketPlayer(name="Lebron", surname="James", height_cm=203, weight_kg=113, points=27.2,
                      rebounds=7.4, assists=7.2)

kevin = BasketPlayer(name="Kevin", surname="Durant", height_cm=211, weight_kg=115, points=26.5,
                     rebounds=7, assists=6)

print(lebron.name)
print(lebron.height_cm)
print(kevin.surname)
print(kevin.weight_kg)

# seznam igralcev
bb_players = [lebron, kevin]

for player in bb_players:
    print(player.name + ", " + player.surname)

# objekti lahko imajo svoje funkcije oz. metode

print(lebron.weight_to_lbs())

class FBPlayer():
    def __init__(self, name, surname, height_cm, weight_kg, goals, y_cards, r_cards):
        self.name = name
        self.surname = surname
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.y_cards = y_cards
        self.r_cards = r_cards


ronaldo = FBPlayer(name="Cristiano", surname="Ronaldo", height_cm=184, weight_kg=79, goals=586,
                   y_cards=95, r_cards=11)

messi = FBPlayer(name="Lionel", surname="Messi", height_cm=170, weight_kg=67, goals=575,
                 y_cards=67, r_cards=0)

print(ronaldo.name)
print(messi.goals)

# če so kategorije iste, lahko kodo iz več classov damo v en class:
class Player():
    def __init__(self, name, surname, height_cm, weight_kg):  # vse skupne kategorije
        self.name = name
        self.surname = surname
        self.height_cm = height_cm
        self.weight_kg = weight_kg

class BasketPlayer(Player):
    def __init__(self, name, surname, height_cm, weight_kg, points, rebounds, assists):  # vse kategorije
        super().__init__(name=name, surname=surname, height_cm=height_cm, weight_kg=weight_kg)  # vse skupne kategorije
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FBPlayer(Player):
    def __init__(self, name, surname, height_cm, weight_kg, goals, y_cards, r_cards):
        super().__init__(name=name, surname=surname, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.y_cards = y_cards
        self.r_cards = r_cards