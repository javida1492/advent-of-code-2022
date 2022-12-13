with open("day8/input.txt") as f:
    lines = f.readlines()

    grid = []

    for line in lines:
        line = line.strip("\n")
        line = list(line)
        converted = [int(num) for num in line]
        grid.append(converted)
        # print(converted)

    print(grid)
