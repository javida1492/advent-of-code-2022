# read initial crate stacks into a dictionary
# dictionary: {stack_num: [boxes]}
# when moving boxes, remove boxes from list and store into a new list
# reverse the list
# add to the end of destination stack
# boxes are always grabbed from the end
# print create from the top of each stack, e.g. the end of the list


# when reading in moves, grab only numbers from the line and store into a list
import re, os
from collections import defaultdict

def process_stacks():
    num_stacks = 9
    with open("input-stacks.txt") as f:
        lines = f.readlines()
        stacks = defaultdict(list)

        for line in lines:
            line = [re.sub(r'[\[\]\n]', '', line[i:i+4].strip(' ')) for i in range(0, len(line), 4)]

            for i in range(0, num_stacks):
                if line[i].strip():
                    stacks[i].insert(0, line[i])
    return stacks

def process_moves(stacks):
    with open("input-moves.txt") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            # line = list(re.sub('[^0-9]', '', line))
            line = list(filter(None, re.sub('[^0-9]', ' ', line).split(' ')))
            #line[1] = source stack
            #line[2] = destination stack
            #line[0] = number of boxes to move
            source_index = int(line[1])-1
            destination_index = int(line[2])-1

            #Get source stack
            boxes = stacks.get(source_index)

            split_index = len(boxes)-int(line[0])
            # Get leftover boxes
            boxes_remaining = boxes[:split_index]
            # Get boxes to move
            boxes_to_move = boxes[split_index:]
            #Reverse boxes to move since we are moving them 1 by 1
            boxes_to_move.reverse()

            stacks[source_index] = boxes_remaining
            stacks[destination_index].extend(boxes_to_move)
            count += 1
            print(count)


    return stacks

def print_top_of_stacks(processed_stacks):

    for i in range(0, len(processed_stacks)):
        print(processed_stacks[i][-1])

def run():
    stacks = process_stacks()
    processed_stacks = process_moves(stacks)
    print_top_of_stacks(processed_stacks)

run()

