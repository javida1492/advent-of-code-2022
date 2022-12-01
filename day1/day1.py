# Time Complexity: O(n) to read each line, O(NlogN) to sort each time but O(N) > O(NlogN) 
# Space Complexity: O(m) since we are using an additional list to store the sums
with open("input.txt") as f:
    lines = f.readlines()

    top_three_sums = []
    cur_sum = 0

    for line in lines:
        if line.strip():
            cur_sum += int(line)
        else:
            if(len(top_three_sums) < 3):
                top_three_sums.append(cur_sum)
                top_three_sums.sort()
            else :
                top_three_sums.append(cur_sum)
                top_three_sums.sort()
                top_three_sums.pop(0)

            cur_sum = 0
        
    max_sum = 0
    for num in top_three_sums:
        max_sum += num

    print(max_sum)

