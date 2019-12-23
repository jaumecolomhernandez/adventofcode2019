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
    RELATIVE = 9 
    RESET = 99

class IntCode:
    """ Implementation of the IntCode computer """

    def __init__(self, numbers, inputs):
        numbers.extend([0]*1024)
        self.ins = numbers
        self.debug = False
        self.index = 0
        self.inputs = inputs
        self.finished = False
        self.output = None
        self.outputs = []
        self.i_n = 0
        self.relative_base = 0
    
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
        params = self.get_vals(modes)   # If invalid returns None for the parameter
        
        #print(self.ins[:15])
        #print(action, modes)
        #print(params)
        
        # Execute actions
        if action is ops.SUM:     # 1 Sum
            #print("SUM")
            self.ins[params[2]] = params[0] + params[1]
            self.index += 4

        elif action is ops.MULTIPLICATION:   # 2 Multiply
            #print("MULTIPLICATION")
            self.ins[params[2]] = params[0] * params[1]
            self.index += 4

        elif action is ops.INPUT:   # 3 Input
            #print("INPUT")
            self.ins[self.get_destination(self.ins[self.index+1], modes[0])] = int(self.inputs.pop(0))
            self.index += 2

        elif action is ops.OUTPUT:   # 4 print
            #print("OUTPUT")
            self.output = params[0]
            self.outputs.append(self.output)
            #print(self.output)
            self.index += 2

        elif action is ops.JUMP_TRUE:   # 5 (!=0)
            #print("JUMP IF TRUE")
            self.index = params[1] if params[0] != 0 else (self.index + 3)

        elif action is ops.JUMP_FALSE:   # 6 (==0)
            #print("JUMP IF FALSE")
            self.index = params[1] if params[0] == 0 else (self.index + 3)

        elif action is ops.LESS_THAN:
            #print("LESS THAN")  
            self.ins[params[2]] = 1 if params[0] < params[1] else 0
            self.index += 4

        elif action is ops.EQUALS:
            #print("EQUALS")   
            self.ins[params[2]] = 1 if params[0] == params[1] else 0
            self.index += 4
        
        elif action is ops.RELATIVE:
            #print("EQUALS")   
            self.relative_base += params[0]
            self.index += 2

        elif action is ops.RESET:
            self.finished = True

    def get_vals(self, modes):
        " Gets the literal parameters "
        params = [None, None, None]
        try: params[0] = self.get_value(self.ins[self.index+1], modes[0])
        except: pass
        try: params[1] = self.get_value(self.ins[self.index+2], modes[1])
        except: pass
        try: params[2] = self.get_destination(self.ins[self.index+3], modes[2])
        except: pass
        return params
    
    def get_value(self, parameter, mode):
        """ Given the parameter and its mode returns the value """
        if mode == 0:   # Position mode
            return self.ins[parameter]
        elif mode == 1: # Immediate mode
            return parameter
        elif mode == 2: # Relative mode
            return self.ins[parameter+self.relative_base]
        else:
            print("Wrong mode")
            return None

    def get_destination(self, parameter, mode):
        """ Given the parameter and its mode returns the value """
        if mode == 0:   # Position mode
            return parameter
        elif mode == 1: # Immediate mode
            print("IMPOSSIBLE!")
            return parameter
        elif mode == 2: # Relative mode
            return parameter+self.relative_base
        else:
            print("Wrong mode")
            return None

    def compute(self):
        """ Runs the whole program until it halts"""
        while not self.finished:
            self.run_op()
    
    def compute_solution(self):
        """ Run program until we have a solution"""
        while not self.finished:
            self.run_op()
            if self.output != None:
                return self.output
        
def run_test(numbers, input_list, output, test_name):
    """ Check that a specific input gives an specific output 
        Params:
        - numbers:      ([int]) instructions
        - input_list:   ([int]) inputs
        - output:       ([int]) values that computer.outputs should match
        - test_name:    (str) just used for representation
        Returns:
        - (int):    1 if correct 0 if incorrect
    """
    inp = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    computer = IntCode(numbers.copy(),input_list)
    computer.compute()
    if computer.outputs == output: print(f"{test_name} PASSED")
    else:   
        print(f"{test_name} NOT PASSED")
        print(computer.outputs)

def run_tests():
    """ Runs a series of tests
        If the computer passes all of them I assume it works
    """
    # Day 5
    inp = [3,9,8,9,10,9,4,9,99,-1,8]
    run_test(inp, [8], [1], "TEST 5.1")
    run_test(inp, [2], [0], "TEST 5.2")
    inp = [3,9,7,9,10,9,4,9,99,-1,8]
    run_test(inp, [7], [1], "TEST 5.3")
    run_test(inp, [8], [0], "TEST 5.4")
    inp = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    run_test(inp, [0], [0], "TEST 5.5")
    run_test(inp, [1], [1], "TEST 5.6")
    inp = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    run_test(inp, [0], [0], "TEST 5.7")
    run_test(inp, [1], [1], "TEST 5.8")
    inp = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    run_test(inp, [0], [0], "TEST 5.9")
    run_test(inp, [1], [1], "TEST 5.10")
    inp = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    run_test(inp, [7], [999], "TEST 5.11")
    run_test(inp, [8], [1000], "TEST 5.12")
    run_test(inp, [9], [1001], "TEST 5.13")
    # Day 7
    # This is sorta complex to do
    # Day 9
    # Day 9.1
    inp = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    #run_test(inp, [], inp, "TEST 9.1")
    # Day 9.2
    inp = [1102,34915192,34915192,7,4,7,99,0]
    run_test(inp, [], [1219070632396864], "TEST 9.2")
    # Day 9.3
    inp = [104,1125899906842624,99]
    run_test(inp, [], [1125899906842624], "TEST 9.3")
    



if __name__ == "__main__":
    input_file = open("input", "r").read()

    numbers = [int(num) for num in input_file.split(',')]
    #numbers = [3,9,8,9,10,9,4,9,99,-1,8]
    computer = IntCode(numbers,[1])
    computer.compute()    
    print(computer.outputs)
    run_tests()
    

    