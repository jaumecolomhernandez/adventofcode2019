#!/usr/bin/env python3

from itertools import combinations

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

    planets = []
    for line in input_file:
        result = [st.strip(' <>\n') for st in line.split(',')]
        planet = {}
        planet['position'] = [int(result[0][2:]), int(result[1][2:]), int(result[2][2:])]
        planet['speed'] = [0, 0, 0]
        planets.append(planet)

    planets_repr(planets,0)
    
    for i in range(1000):
        for two_planet in combinations(planets, 2):
            compute_gravity(two_planet[0],two_planet[1])
        for planet in planets:
            apply_speed(planet)
        
        planets_repr(planets,i+1)
        print(f"Energy of the system: {compute_energy(planets)}")
