with open("dna.txt", "r") as dna:
    dna = dna.read()
    print(dna)


people = {"Eva": ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "Larisa": ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"],
          "Matej": ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"],
          "Miha": ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]}

for person in people:
    suspect = True
    for prop in people[person]:
        if prop not in dna:
            suspect = False
            break
    if suspect is True:
        print("{} is our perpetrator!".format(person.upper()))




