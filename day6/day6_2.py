#!/usr/bin/env python3

# Approach 1
# Count the steps from the single childs
# Approach 2
# Tree traversal and count
# See comment in main

class Graph:
    def __init__(self, edge_list):
        self.edges = edge_list

        # Create unique nodes
        flat_list = [item for sublist in self.edges for item in sublist]
        list_set = set(flat_list)  
        self.unique = (list(list_set))

        # Create matchs dictionary
        self.matchs = dict()
        self.size = len(self.unique)
        for (item, i) in zip(self.unique, range(self.size)): self.matchs[item] = i

        # Create matrix
        self.adjacency = [[0]*self.size for _ in range(self.size)]
        # Fill matrix
        for sink, source in self.edges:
            self.adjacency[self.matchs[sink]][self.matchs[source]] = 1
            self.adjacency[self.matchs[source]][self.matchs[sink]] = 1
        

    def print(self):
        print(' '.join(self.unique))
        print(' '+'\n '.join(['   '.join([str(cell) for cell in row]) for row in self.adjacency]))


    # The following djikstra implementation is from geeksforgeeks.com
    # Link -> https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

    def minDistance(self, dist, sptSet): 
        # Initilaize minimum distance for next node 
        min = float("inf")
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.size): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
    
    def djikstra(self, origin):
        dist = [float("inf")] * self.size 
        dist[origin] = 0
        sptSet = [False] * self.size

        for count in range(self.size): 
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shortest path tree 
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.size): 
                if  (self.adjacency[u][v] > 0) and \
                    (sptSet[v] == False) and \
                    (dist[v] > dist[u] + self.adjacency[u][v]): 
                        dist[v] = dist[u] + self.adjacency[u][v]    
        return dist

def edge_list(input_file):
    links = list()
    # Create directed graph
    for line in input_file:        
        links.append([line[:3], line[4:7]])
    return links


if __name__ == "__main__":
    # In the previous challenge I represented the galaxy as a tree.
    # For this problem it is necessary to represent it as a graph.
    # So will be creating an adjacency matrix and then run djikstra on it.

    # Read different links
    input_file = open("input", "r")
    edges = edge_list(input_file)

    g = Graph(edges) # Create graph

    #g.print()
    dist = g.djikstra(g.matchs['YOU']) # Run djikstra

    #print(dist)
    print(dist[g.matchs['SAN']]-2) # We subtract the orbits (2)

    
