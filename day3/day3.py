# with open("input.txt") as f:
# Part 1
# lines = f.readlines()
# sum_of_types = 0

# for line in lines:
#     firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]

#     dict = {}
#     shared = set()
#     secondpart = secondpart.replace("\n", "")

#     for c in firstpart:
#         dict[c] = 1

#     for c in secondpart:
#         if dict.get(c) == 1:
#             shared.add(c)

#     for c in shared:
#         if c.islower():
#             sum_of_types += ord(c) - 96
#         else:
#             sum_of_types += ord(c) - 38

# print(sum_of_types)

#####################

# Part 2
from itertools import islice


def get_shared_chars(next_n_lines):
    shared = set()
    for line in next_n_lines:
        uniquified = set(line.replace("\n", ""))
        if len(shared) == 0:
            shared = uniquified
        else:
            shared = uniquified.intersection(shared)
    return shared


def get_priority_value(characters):
    sum_of_priorities = 0
    for c in characters:
        if c.islower():
            sum_of_priorities += ord(c) - 96
        else:
            sum_of_priorities += ord(c) - 38
    return sum_of_priorities


with open("input.txt") as f:
    sum_of_priorities = 0
    while True:
        next_n_lines = list(islice(f, 6))
        if not next_n_lines:
            break

        shared_group_1 = get_shared_chars(next_n_lines[0:3])
        shared_group_2 = get_shared_chars(next_n_lines[3:6])
        sum_of_priorities += get_priority_value(shared_group_1)
        sum_of_priorities += get_priority_value(shared_group_2)

    print(sum_of_priorities)
