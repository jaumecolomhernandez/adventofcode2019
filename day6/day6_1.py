#!/usr/bin/env python3

# Approach 1
# Count the steps from the single childs
# Approach 2
# Tree traversal and count

class planet:
    def __init__(self, name):
        self.name = name
        self.links = list()
    
    def __repr__(self):
        return f"{self.name}-{self.links}"

def create_graph(input_file):
    planets = dict()
    # Create directed graph
    for line in input_file:
        
        o = line[:3]
        d = line[4:7]

        if o in planets:
            origin = planets[o]
        else:
            origin = planet(o)
            planets[o] = origin

        if d in planets:
            destination = planets[d]
        else:
            destination = planet(d)
            planets[d] = destination
        
        origin.links.append(destination)
    
    return planets

def traverse(head):
    " Prints name and calls on its children "
    planet = head
    print(planet.name, end="")
    for i in range(len(planet.links)):
        #print(" -> ", end="")
        print("")
        traverse(planet.links[i])
    
def traverse2(head):
    " Prints name and links for each "
    planet = head
    print(planet.name ,end="")
    for i in range(len(planet.links)): print( ' ->',planet.links[i].name,end="")
    print("")
    for i in range(len(planet.links)): traverse2(planet.links[i])

def count(planet, counter):
    " Traversal and keeps count "
    counter += 1
    actual = counter
    for i in range(len(planet.links)): 
        counter += count(planet.links[i], actual)
    return counter - 1 # For whatever reason we must subtract the number of planets

if __name__ == "__main__":
    # Read different links
    input_file = open("input", "r")
    planets = create_graph(input_file)
    head = planets['COM']
    # traverse2(head)
    print(count(head,0))
