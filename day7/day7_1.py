#!/usr/bin/env python3
import itertools
from enum import Enum


class ops(Enum):
    SUM = 1
    MULTIPLICATION = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_TRUE = 5
    JUMP_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    RESET = 99

class IntCode:
    """ Implementation of the IntCode computer """
    def __init__(self, numbers, inputs):
        self.ins = numbers
        self.debug = False
        self.index = 0
        self.inputs = inputs
        self.finished = False
        self.output = None
        
    def run_tests(self):
        pass
    
    def debug_print(self, text):
        if self.debug: print(text)
    
    def convert(self, action):
        """ Converts instruction to operation and modes """
        action = [int(n)for n in str(action)]
        while len(action)!=5:
            action.insert(0,0)
        # Get values array
        values = [10*action[3]+action[4],0,0,0]
        values[1] = action[2] 
        values[2] = action[1] 
        values[3] = action[0]

        return ops(values[0]), values[1:]
    
    def run_op(self):
        action, modes = self.convert(self.ins[self.index])
    
        # Compute parameters
        if action not in [ops.INPUT, ops.OUTPUT, ops.RESET]:
            first, second = self.get_vals(modes)

        # Execute actions
        if action is ops.SUM:     # 1 Sum
            #print("SUM")
            self.ins[self.ins[self.index+3]] = first + second
            self.index += 4

        elif action is ops.MULTIPLICATION:   # 2 Multiply
            #print("MULTIPLICATION")
            self.ins[self.ins[self.index+3]] = first * second
            self.index += 4

        elif action is ops.INPUT:   # 3 Input
            #print("INPUT")
            self.ins[self.ins[self.index+1]] = int(self.inputs.pop(0))
            self.index += 2

        elif action is ops.OUTPUT:   # 4 print
            #print("OUTPUT")
            #print(self.ins[self.ins[self.index+1]])
            self.output = self.ins[self.ins[self.index+1]]
            self.index += 2

        elif action is ops.JUMP_TRUE:   # 5 (!=0)
            #print("JUMP IF TRUE")
            self.index = second if first != 0 else (self.index + 3)

        elif action is ops.JUMP_FALSE:   # 6 (==0)
            #print("JUMP IF FALSE")
            self.index = second if first == 0 else (self.index + 3)

        elif action is ops.LESS_THAN:
            #print("LESS THAN")  
            self.ins[self.ins[self.index+3]] = 1 if first < second else 0
            self.index += 4

        elif action is ops.EQUALS:
            #print("EQUALS")   
            self.ins[self.ins[self.index+3]] = 1 if first == second else 0
            self.index += 4

        elif action is ops.RESET:
            self.finished = True
            self.index += 1


    
    def get_vals(self, modes):
        " Only used when two parameters needed "
        first = self.ins[self.index+1] if modes[0] else self.ins[self.ins[self.index+1]]
        second = self.ins[self.index+2] if modes[1] else self.ins[self.ins[self.index+2]]
        return first, second

    def compute(self):
        """ Runs the whole program until it halts"""

        while not self.finished:
            self.run_op()
            
            
  

if __name__ == "__main__":
    input_file = open("test", "r").read()

    numbers = [int(num) for num in input_file.split(',')]

    
    max_out = 0
    for comb in itertools.permutations([5,6,7,8,9]):
    
        output = 0
        for i in range(5):
            computer = IntCode(numbers,[comb[i], output])
            computer.compute()
            output = computer.output
        if max_out < output:
            max_out = output
        
    
    print(max_out)

    