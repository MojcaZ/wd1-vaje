x = 5
y = 2
print(x + y)

string_a = "Hello,"
string_b = "World!"
print(string_a + " " + string_b)

user_name = input("Enter your name: ").title() #povemo, naj ima input velike začetnice
print("Hello, " + user_name + "!")

first_num = int(input("Enter the first number: ")) #povemo, da bo input integer
second_num = int(input("Enter the second number: "))
print(first_num + second_num)

mood = "happy"
if mood == "happy":
    print("I'm happy.")
elif mood == "sad":
    print("I'm sad.")
else:
    print("I'm not happy.")
