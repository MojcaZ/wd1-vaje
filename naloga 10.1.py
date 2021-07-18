
with open("people.csv", "r") as people_file:
    contents = people_file.read().splitlines()

    for line in contents:
        line_data = line.split(",")
        print("{0} is {1} years old and {2}.".format(line_data[0], line_data[1], line_data[2]))