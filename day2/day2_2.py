#!/usr/bin/env python3
input_file = open("input", "r").read()

base_numbers = [int(num) for num in input_file.split(',')]

def compute_inputs(noun, verb):
    # Vars
    run = True
    i = 0
    # Compute input
    numbers = base_numbers.copy()
    numbers[1] = noun
    numbers[2] = verb
    # Compute
    while(run):
        if numbers[i] == 1:
            numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
            i = i + 4
        elif numbers[i] == 2:
            numbers[numbers[i+3]] = numbers[numbers[i+1]] * numbers[numbers[i+2]]
            i = i + 4
        elif numbers[i] == 99:
            run = False
            i = i + 1
    
    return numbers[0]

if __name__ == "__main__":
    for i,j in ((a,b) for a in range(100) for b in range(100)):
        if compute_inputs(i,j) == 19690720 : break
    print(i,j)
