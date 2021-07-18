# odpremo povezavo s txt-filom
ninja_file = open("ninja.txt", "r")

contents = ninja_file.read()
print(contents)

# zapremo povezavo s txt-filom
ninja_file.close()

# rezultat je enak kot zgoraj, povezava se zapre sama. priporočljiv način
with open("ninja.txt", "r") as ninja_file:
    contents = ninja_file.read()
    print(contents)

# enako lahko naredimo s for-loopom
with open("ninja.txt", "r") as ninja_file:
    ninja_lines = ninja_file.read().splitlines()

    for line in ninja_lines:
        print(line)

# pisanje v file. če file ne obstaja, ga usvari

with open("ninja.txt", "a") as ninja_file: #"a" za dodajanje, "w" za prepisovanje
    ninja_file.write("\nHello?")  # za dodajanje teksta