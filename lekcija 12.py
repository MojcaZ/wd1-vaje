def hello(name):
    print("Hello, {0}!".format(name))  # dodamo parametre za vnos podatkov

    
hello("Matt")


def say_hello(name):
    return "Hello, {0}!".format(name)


text = say_hello("Matt")  # rezultat shranimo v variabli
print(text)

# ali
print(say_hello("Matt"))


def sum(num1, num2):
    result = num1 + num2
    return result


print(sum(4,5))


def cube(num):
    result = num * num * num
    return result


print(cube(5))

#  števec korakov
def step_calc(dist, step_length):
    steps_made = dist / step_length
    return int(steps_made)


print(step_calc(100, 0.3))


#  absolutna razlika med številkama
def absolute_difference(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1


print(absolute_difference(3, 5))
print(absolute_difference(10, 6))