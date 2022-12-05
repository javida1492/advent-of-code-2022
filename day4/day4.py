import re
with open("input.txt") as f:
    lines = f.readlines()

    overlapped_pairs = 0

    for line in lines:
        line = [int(x) for x in re.split(r'[,-]', line.strip('\n'))]

        if line[0] <= line[2] and line[1] >= line[2]:
            overlapped_pairs += 1
        elif line[2] <= line[0] and line[3] >= line[0]:
            overlapped_pairs += 1
        elif line[0] <= line[2] and line[1] <= line[3] and line[1] >= line[2]:
            overlapped_pairs += 1
        elif line[2] <= line[0] and line[3] >= line[1]:
            overlapped_pairs += 1

    print(overlapped_pairs)
