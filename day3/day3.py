import os

print(os.getcwd())
with open("input.txt") as f:
    lines = f.readlines()

    sum_of_types = 0

    for line in lines:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]

        dict = {}
        shared = set()
        secondpart = secondpart.replace("\n", "")

        for c in firstpart:
            dict[c] = 1

        for c in secondpart:
            if dict.get(c) == 1:
                shared.add(c)

        for c in shared:
            if c.islower():
                sum_of_types += ord(c) - 96
            else:
                sum_of_types += ord(c) - 38

    print(sum_of_types)
