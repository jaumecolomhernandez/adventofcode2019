#!/usr/bin/env python3
import time
from enum import Enum

class ops(Enum):
    SUM = 1
    MULTIPLICATION = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    RESET = 99


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

    time.sleep(0.05)
    #print(values)

    return ops(values[0]), values[1:]

def get_values(i,modes,nvalues):
    """ Gets values """ # UNUSED
    values = [0]*nvalues
    for j in range(nvalues-1):
        values[j] = numbers[i+1+j] if modes[j] else numbers[numbers[i+1+j]]
    values[nvalues-1] = numbers[i+nvalues] 
 
    return values

def compute(numbers):
    """Runs the whole program"""
    i = 0
    run = True
    while(run):
        # Get action and modes of the call
        action, modes = convert(numbers[i])
        print(action, modes)
        # Execute actions
        if action is ops.SUM:     # 1 Sum
            first = numbers[i+1] if modes[0] else numbers[numbers[i+1]]
            second = numbers[i+2] if modes[1] else numbers[numbers[i+2]]
            numbers[numbers[i+3]] = first + second
            i = i + 4
        elif action is ops.MULTIPLICATION:   # 2 Multiply
            first = numbers[i+1] if modes[0] else numbers[numbers[i+1]]
            second = numbers[i+2] if modes[1] else numbers[numbers[i+2]]
            numbers[numbers[i+3]] = first * second
            i = i + 4
        elif action is ops.INPUT:   # 3 Input
            inp = input("WRITE ID => ")
            numbers[numbers[i+1]] = int(inp)
            i = i + 2
        elif action is ops.OUTPUT:   # 4 print
            print(numbers[numbers[i+1]])
            i = i + 2
        elif action is ops.JUMP_IF_TRUE:   # 5 (!=0)
            
            first = numbers[i+1] if modes[0] else numbers[numbers[i+1]]
            second = numbers[i+2] if modes[1] else numbers[numbers[i+2]]
            i = second if first != 0 else (i + 3)
        elif action is ops.JUMP_IF_FALSE:   # 6 (==0)
            first = numbers[i+1] if modes[0] else numbers[numbers[i+1]]
            second = numbers[i+2] if modes[1] else numbers[numbers[i+2]]
            i = second if first == 0 else (i + 3)
        elif action is ops.LESS_THAN:  
            first = numbers[i+1] if modes[0] else numbers[numbers[i+1]]
            second = numbers[i+2] if modes[1] else numbers[numbers[i+2]]
            numbers[numbers[i+3]] = 1 if first < second else 0
            i = i + 4
        elif action is ops.EQUALS:   
            first = numbers[i+1] if modes[0] else numbers[numbers[i+1]]
            second = numbers[i+2] if modes[1] else numbers[numbers[i+2]]
            numbers[numbers[i+3]] = 1 if first == second else 0
            i = i + 4
        elif action is ops.RESET:
            run = False
            i = i + 1
  

if __name__ == "__main__":
    input_file = open("input", "r").read()

    numbers = [int(num) for num in input_file.split(',')]

    compute(numbers)
    