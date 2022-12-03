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

        # Lose
        if choices[1] == 'X':
            if choices[0] == 'A': score += 3
            elif choices[0] == 'B': score += 1
            else: score += 2
        # Draw
        if choices[1] == 'Y':
            if choices[0] == 'A': score += 1
            elif choices[0] == 'B': score += 2
            else: score += 3
            score += 3
        # Win
        elif choices[1] == 'Z':
            if choices[0] == 'A': score += 2
            elif choices[0] == 'B': score += 3
            else: score += 1
            score += 6

    print(score)