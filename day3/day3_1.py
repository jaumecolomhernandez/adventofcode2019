#!/usr/bin/env python3

# Read file
input_file = open("input", "r")
first = input_file.readline().split(',')
second = input_file.readline().split(',')

# Create tableboard
zx,zy = 14000,14000
table = [[0]*zx for i in range(zy)] # Python lists take a lot of time to create :o
pos = [zx//2, zy//2]

def print_table(table):
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
    for move in first:
        direction = move[0]
        num = int(move[1:])

        for i in range(1,num+1):
            pos = update_pos(direction, pos)
            table[pos[0]][pos[1]] += 1

    # Reset table
    pos = [zx//2, zy//2]
    distance = 10000000000000
    results = []

    # Find painted positions
    for move in second:
        direction = move[0]
        num = int(move[1:])

        # Basically iterate every position and find out if it 
        # is painted. Then repeat for all 
        for i in range(1,num+1):
            pos = update_pos(direction, pos)
            if table[pos[0]][pos[1]] == 1: results.append(abs(pos[0]-zx//2)+abs(pos[1]-zy//2))
                
    print(min(results))





