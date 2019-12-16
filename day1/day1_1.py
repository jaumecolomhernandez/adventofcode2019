#!/usr/bin/env python3

input_file = open("input", "r")
fuel = 0

for line in input_file:
    fuel += int(line)//3-2

print(fuel)