#!/usr/bin/env python3

input_file = open("input", "r")
fuel = 0

def compute_fuel(mass):
    f = mass//3-2
    if f>0:
        ff = compute_fuel(f)
        if ff>0: f += ff
    
    return f

for line in input_file:
    fuel += compute_fuel(int(line))

print(fuel)