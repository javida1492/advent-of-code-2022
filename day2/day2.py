with open("input.txt") as f:
    lines = f.readlines()

    dict = {
        'A': 1, #rock
        'B': 2, #paper
        'C': 3, #scissors
        'X': 1, #rock
        'Y': 2, #paper
        'Z': 3, #scissors
    }

    # rock > scissors
    # paper > rock
    # scissors > paper

    score = 0
    for line in lines:
        choices = line.split()

        if choices[1] == 'X':
            if choices[0] == 'A': score += 3
            elif choices[0] == 'C': score += 6
        elif choices[1] == 'Y':
            if choices[0] == 'B': score += 3
            elif choices[0] == 'A': score += 6
        elif choices[1] == 'Z':
            if choices[0] == 'C': score += 3
            elif choices[0] == 'B': score += 6

        # Add choice
        score += dict.get(choices[1])

    print(score)