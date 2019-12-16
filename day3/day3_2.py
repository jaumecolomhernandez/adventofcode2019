#!/usr/bin/env python3

import numpy as np

# Read file
input_file = open("input", "r")
first = input_file.readline().split(',')
second = input_file.readline().split(',')

# Create tableboard
zx,zy = 14000,14000
table = np.zeros((zx,zy,2), dtype=np.int32) # Numpy works perfect
#table = [[[0,0] for j in range(zx)] for i in range(zy)] # Python lists take a lot of time to create :o
pos = [zx//2, zy//2]

def print_table():
    "Prints table"
    for line in table:
        print(line)

def update_pos(direction, pos):
    "Moves position according to direction"
    if direction == 'U':
        pos = [pos[0]-1,pos[1]]
    elif direction == 'R':
        pos = [pos[0],pos[1]+1]
    elif direction == 'D':
        pos = [pos[0]+1,pos[1]]
    elif direction == 'L':
        pos = [pos[0],pos[1]-1]

    return pos

if __name__ == "__main__":
    # Paint table
    step = 0
    for move in first:
        direction = move[0]
        num = int(move[1:])

        for i in range(1,num+1):
            pos = update_pos(direction, pos)
            table[pos[0]][pos[1]][0] += 1
            step += 1
            table[pos[0]][pos[1]][1] = step

    # Reset table
    pos = [zx//2, zy//2]
    distance = 100000000000
    results = []
    step = 0
    # Find painted positions
    for move in second:
        direction = move[0]
        num = int(move[1:])

        # Basically iterate every position and find out if it 
        # is painted. Then repeat for all 
        for i in range(1,num+1):
            pos = update_pos(direction, pos)
            step += 1
            if table[pos[0]][pos[1]][0] == 1:
                results.append(table[pos[0]][pos[1]][1] + step)
 
    print(min(results))





