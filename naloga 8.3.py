
num_one = int(input("Enter the first number:\n"))
num_two = int(input("Enter the second number:\n"))
operation = input("Enter +, -, * or /.\n")

if operation == "+":
    print(num_one + num_two)
elif operation == "-":
    print(num_one - num_two)
elif operation == "*":
    print(num_one * num_two)
elif operation == "/":
    print(num_one / num_two)
else:
    print("This is not a valid operation.")