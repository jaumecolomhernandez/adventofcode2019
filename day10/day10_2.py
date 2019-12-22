#!/usr/bin/env python3
import math

if __name__ == "__main__":

    input_file = open("input", "r").read()
    inputt = [list(line) for line in input_file.split('\n')]

    # Very important (Base)
    base = (22,17)
    
    # 1- Get list of differents asteroids
    asteroids = []
    for i,j in ((n,m) for n in range(len(inputt)) for m in range(len(inputt[0]))):
        if inputt[i][j] == '#': asteroids.append((i,j))
    
    # 2- Get dict with the different direction vectors
    directions = dict()
    for asteroid in asteroids:
        direction = (asteroid[0]-base[0],
                        asteroid[1]-base[1])
        if direction == (0,0): continue
        
        count = 0
        for result in directions.keys():   # Check if directions are the same
            # In case they are stop
            if ((direction[0]*result[1]-direction[1]*result[0]) == 0) and ((direction[0]>0) == (result[0]>0)) and ((direction[1]>0) == (result[1]>0)): 
                directions[result].append(direction)
                break
            else: count += 1
        if count == len(directions):    # If none parallel -> append to list
            directions[direction] = [direction]
    print(directions)

    # 3- Sort by phi
    phis = dict()
    for key in directions.keys():
        # Bc it returns atan*2 also the degrees are multiplied by two
        phi = ((math.atan2(key[1],key[0 ])/math.pi*180+180+360)%360)
        # Stored in hashmap for easy retrieval
        phis[phi] = key
    sorted_keys = sorted(phis.keys(), reverse=True)
    sorted_keys.insert(0,sorted_keys.pop())
    # This is a list with sorted lists of direction vectors of the same phi (different length)
    directions = [directions[phis[key]] for key in sorted_keys]
    
    # 4- Sort by length
    final_dirs = []
    for direction_set in directions:
        print(direction_set)
        # R2 distance
        final_dirs.append(sorted(direction_set, key=lambda dir: (dir[0]**2+dir[1]**2)**0.5)) 

    #print(final_dirs)

    # Cool setup with ncurses to visualize the evolution of the asteroid destruction
    import curses
    import time
    mywindow = curses.initscr()
    def create_st(inputt):
        pr = ""
        for st in inputt:
            pr += ' '.join(st)+'\n'
        return pr
    
  
    i = 0
    c = 0
    while c != 200:
    #while (len(final_dirs)>1) or ((len(final_dirs) == 1) and (len(final_dirs[0])>1)):   # This is to visualize until the end     
        # Calculation
        d = final_dirs[i].pop(0)
        pos = (base[0]+d[0],base[1]+d[1])

        # Representation
        inputt[pos[0]][pos[1]] = "O"
        mywindow.addstr(3,0, create_st(inputt))
        mywindow.refresh()
        time.sleep(0.03)
        inputt[pos[0]][pos[1]] = "."

        # Pointer arithmetic        
        if len(final_dirs[i])==0:  final_dirs.pop(i)
        else: i += 1
        
        if i == len(final_dirs): i = 0 
        c += 1

    curses.endwin()
    print(c)
    obj = final_dirs[i].pop(0)
    print(obj)
    pos = (base[0]+d[0],base[1]+d[1])
    
    inputt[pos[0]][pos[1]] = "O"
    print(pos)
    print("Final solution -> ", pos[1]*100 + pos[0])

    
        
        
        