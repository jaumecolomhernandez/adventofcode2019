#!/usr/bin/env python3

if __name__ == "__main__":

    input_file = open("input", "r").read()

    print(input_file)
    a = [list(line) for line in input_file.split('\n')]

    # 1- Get list of differents asteroids
    asteroids = []
    for i,j in ((n,m) for n in range(len(a)) for m in range(len(a[0]))):
        if a[i][j] == '#': asteroids.append((j,i))

    # 2- Count number of insight asteroids (N3) very slow implementation :(
    nums = []
    for asteroidA in asteroids:
        directions = []
        for asteroidB in asteroids:
            
            direction = (asteroidA[0]-asteroidB[0],
                         asteroidA[1]-asteroidB[1])
            if direction == (0,0): continue
            
            count = 0
            for result in directions:   # Check if directions are the same
                # In case they are stop
                if ((direction[0]*result[1]-direction[1]*result[0]) == 0) and ((direction[0]>0) == (result[0]>0)): break
                else: count += 1
            if count == len(directions):    # If none parallel -> append to list
                directions.append(direction)

        nums.append(len(directions))
        print(asteroidA, len(directions), end="|")
    print(max(nums), asteroids[nums.index(max(nums))])   # Weird bug I need to add one to get the correct result
    