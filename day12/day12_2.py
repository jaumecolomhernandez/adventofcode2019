#!/usr/bin/env python3

from itertools import combinations
import copy

def compute_gravity(planet1, planet2):
    pos1 = planet1['position'].copy()
    pos2 = planet2['position'].copy()
    for i in range(3):
        if pos1[i]>pos2[i]:
            planet1['speed'][i] += -1
            planet2['speed'][i] += 1
        elif pos1[i]<pos2[i]:
            planet1['speed'][i] += 1
            planet2['speed'][i] += -1
    return

def apply_speed(planet):
    for i in range(3):
        planet['position'][i] += planet['speed'][i]
    return

def planets_repr(planets,num):
    print(F"Step {num}")
    for plan in planets:
        print(plan)

def compute_energy(planets):
    energy = 0
    for planet in planets:
        energy += (
            abs(planet['position'][0])
            + abs(planet['position'][1])
            + abs(planet['position'][2]))*(
            abs(planet['speed'][0])
            + abs(planet['speed'][1])
            + abs(planet['speed'][2])
        )
    return energy

if __name__ == "__main__":

    input_file = open("input", "r")

    # Load from file
    planets = []
    for line in input_file:
        result = [st.strip(' <>\n') for st in line.split(',')]
        planet = {}
        planet['position'] = [int(result[0][2:]), int(result[1][2:]), int(result[2][2:])]
        planet['speed'] = [0, 0, 0]
        planets.append(planet)

    og = copy.deepcopy(planets)

    # Find the periodicity of speed components (by grouped dimension)
    periods = []
    #for i in range(3):
    #    planets = copy.deepcopy(og)
    #    planets_repr(planets,2)
    i = 0
    jumps = [0]
    for n in range(1,10000000):
        for two_planet in combinations(planets, 2):
            compute_gravity(two_planet[0],two_planet[1])
        for planet in planets:
            apply_speed(planet)


        if (planets[0]['position'][i] == og[0]['position'][i]) and \
        (planets[1]['position'][i] == og[1]['position'][i]) and \
        (planets[2]['position'][i] == og[2]['position'][i]) and \
        (planets[3]['position'][i] == og[3]['position'][i]):
        # if (planets[i]['position'][0] == og[i]['position'][0]) and \
        # (planets[i]['position'][1] == og[i]['position'][1]) and \
        # (planets[i]['position'][2] == og[i]['position'][2]):
            #planets_repr(planets,n)
            print(f"This is the current period {(n-jumps[-1])}")
            jumps.append(n)
            
    print(jumps)

    # Find MCM
    from math import gcd
""" 
    def lcm(x, y):
        return x * y // gcd(x, y)
    print(lcm(periods[0], lcm(periods[1],periods[2]))) """