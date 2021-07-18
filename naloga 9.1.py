
print("To je pretvornik enot za pretvarjanje kilometrov v milje.")

while True:
    km = input("Vnesi kilometre: \n")
    km = float(km.replace(",", "."))
    miles = km * 0.621
    print(str(km).replace(".", ",") + " kilometrov je " + str(miles).replace(".", ",") + " milje.")
    answer = input("Nova pretvorba? DA/NE \n").upper()
    if answer == "NE" or answer == "N":
        print("Hvala za sodelovanje.")
        break
