with open("input.txt") as f:
    lines = f.readlines()

    cur_sum = 0
    max_sum = 0

    for line in lines:
        if line.strip():
            cur_sum += int(line)
        else:
            if cur_sum > max_sum:
                max_sum = cur_sum
            cur_sum = 0
        
    print(max_sum)