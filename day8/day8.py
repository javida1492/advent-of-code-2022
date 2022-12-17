with open("input.txt") as f:
    lines = f.readlines()

    col_size = len(lines[0].strip("\n"))
    row_size = len(lines)

    grid = []
    # Minimum visible cells will be the edges
    visible = (row_size*2) + (col_size*2) - 4

    for line in lines:
        line = line.strip("\n")
        line = list(line)
        converted = [int(num) for num in line]
        grid.append(converted)

    # Iterate through inner cells
    for row in range (1, row_size-1):
        for col in range(1, col_size-1):
            cell = grid[row][col]

            # Get all horizontal and verticle trees
            left = [grid[row][col-i] for i in range(1, col+1)]
            right = [grid[row][col+i] for i in range(1, col_size-col)]
            up = [grid[row-i][col] for i in range(1, row+1)]
            down = [grid[row+i][col] for i in range(1, row_size-row)]

            # Part 1
            # Check if tallest tree on all sides is greater than current tree
            if max(left) < cell or max(right) < cell or max(up) < cell or max(down) < cell:
                visible += 1

    print(visible)
