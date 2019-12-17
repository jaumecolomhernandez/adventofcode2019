#!/usr/bin/env python3
import time

input_file = open("input", "r").read()

numbers = [int(num) for num in input_file.split(',')]


def convert(action):
    """ Returns action and modes """
    action = [int(n)for n in str(action)]
    while len(action)!=5:
        action.insert(0,0)
    
    # Get values array
    values = [10*action[3]+action[4],0,0,0]
    values[1] = action[2] 
    values[2] = action[1] 
    values[3] = action[0] 

    #print(values)

    return values[0], values[1:]

def get_values(i,modes):
    """ Gets values """
    values = [0,0,0]
    values[0] = numbers[i+1] if modes[0] else numbers[numbers[i+1]]
    values[1] = numbers[i+2] if modes[1] else numbers[numbers[i+2]]
    values[2] = numbers[i+3] 

    return values

input_n = 1

i = 0
run = True
while(run):
    # Get action and modes of the call
    action, modes = convert(numbers[i])

    # In case it needs values, get values
    if action in [1,2]:
        values = get_values(i,modes)
    
    # Execute actions
    if action == 1:     # Sum
        numbers[values[2]] = values[0] + values[1]
        i = i + 4
    elif action == 2:   # Multiply
        numbers[values[2]] = values[0] * values[1]
        i = i + 4
    elif action == 3:   # Input
        numbers[numbers[i+1]] = input_n
        i = i + 2
    elif action == 4:   # Output (print)
        print(numbers[numbers[i+1]])
        i = i + 2
    elif action == 99:
        run = False
        i = i + 1