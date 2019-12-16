#!/usr/bin/env python3

input_file = open("input", "r").read()

numbers = [int(num) for num in input_file.split(',')]

run = True
i = 0
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

print(numbers)