#!/usr/bin/env python3
from math import ceil

def add_ingred(name, ingredients, minimum):
    """ Add material to the recipe book 
        All materials contain the ingredients and the mininum
        amount you have to produce.
        The ingredients are normalized to one unit.
        The material is accessed by the name.
    """
    material = {}
    material['ingredients'] = ingredients
    material['unit'] = int(minimum)
    material['want'] = 0
    material['used'] = 0
    recipe_book[name] = material

    return material # Not used

def parse_input():
    for line in input_file:
        arguments = line.split('=>')[0].strip()
        result = line.split('=>')[1].strip()
        
        arguments = arguments.split(', ')
        result = result.split(' ')
        
        temp_ingredients = []

        for arg in arguments:
            if arg.split(' ')[1] == 'ORE': basic_args.append(result[1])
            temp_ingredients.append((int(arg.split(' ')[0]), arg.split(' ')[1]))
            
        add_ingred(result[1], temp_ingredients, result[0])

def print_recipe_book():
    for key in recipe_book.keys():
        print(f"{key}-{recipe_book[key]}")


class Graph:
    " The only purpose of this class is to sort the classes"
    def __init__(self, recipe_book):
        # Create and populate material dictionary
        self.adj = {name:[] for name in recipe_book.keys()}
        for material in recipe_book.keys():
            for destination in recipe_book[material]['ingredients']:
                self.adj[material].append(destination[1]) 
        # Visited dict for the topological sort
        self.visited = { name: False for name in recipe_book.keys()}
        # Add the ORE material
        self.adj['ORE'] = []
        self.visited['ORE'] = False
        # Output of the sorting
        self.output = []
    
    # Topological sort function taken from
    # Link: https://kushalvyas.github.io/graph_py.html
    def toposort(self, name):
        self.visited[name] = True
        for each in self.adj[name]:
            if not self.visited[each]:
                self.toposort(each)
        
        self.output.append(name)

    def toposort_gen(self):
        for item in self.adj.keys():
            if not self.visited[item]:
                self.toposort(item)
        self.output = list(reversed(self.output))
        
recipe_book = {}

if __name__ == "__main__":
    input_file = open("input", "r")

    
    basic_args = [] # This list contains the names that stop the recursive function

    # Parse the input
    parse_input() # -> recipe_book and basic_args 
    # Create adjacency list
    g = Graph(recipe_book)
    g.toposort_gen()
    
    print(g.output)
    
    recipe_book['FUEL']['want'] = 1
    recipe_book['cost'] = 0
    def compute_cost(name):
        material = recipe_book[name]
        number = ceil(material['want']/material['unit'])
        print(name, material, number)
        for ingredient in material['ingredients']:
            if ingredient[1] == 'ORE':
                print(f"Need {ingredient[0]*number}")
                recipe_book['cost'] += ingredient[0]*number
                return 
            print(f"Added {ingredient[0]*number} to {ingredient[1]} desired quantity")
            recipe_book[ingredient[1]]['want'] += ingredient[0]*number
            #compute_cost(ingredient[1],quantity)
    
    
    for name in g.output[:-1]:
        compute_cost(name)
        
    print(recipe_book['cost'])



    

    
    
    