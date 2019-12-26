#!/usr/bin/env python3

import numpy as np
from math import ceil

def create_base_base(iter):
    " Create single lines (iter,1) "
    patt = np.zeros(iter*4, dtype=int)
    c = 0
    for i in [0,1,0,-1]:
        for j in range(iter):
            patt[c] = i
            c += 1
    return patt

def base_pattern(size):
    " Creates the whole matrix (size, size) "
    base = np.zeros([size, size], dtype=int)
    for i in range(1,size):
        t = create_base_base(i)
   
        if t.shape[0] < (size):
            n = ceil((size)/t.shape[0])
            t = np.tile(t,n)
            
        base[i-1,:] = t[:size]
    return base

def compute_next(digits, base):
    result = np.zeros(len(digits), dtype=int)

    mult = np.transpose(base[:-1, 1:])
    
    result = digits.dot(mult)

    result = abs(result)%10

    return result

if __name__ == "__main__":
    
    digits = 59777098810822000809394624382157501556909810502346287077282177428724322323272236375412105805609092414782740710425184516236183547622345203164275191671720865872461284041797089470080366457723972985763645873208418782378044815481530554798953528896905275975178449123276858904407462285078456817038667669183420974001025093760473977009037844415364079145612611938513254763581971458140349825585640285658557835032882311363817855746737733934576748280568150394709654438729776867932430014255649458605325527757230466997043406136400716198065838842158274093116050506775489075879316061475634889155814030818530064869767243196343272137745926937355015378474209347100518533
    digits = list(map(int,str(digits)))
    digits = np.array(digits,dtype=int)

    base = base_pattern(len(digits)+1)
    print(base)
    
    for _ in range(100):
        digits = compute_next(digits, base)
        #print(digits[0:8])
    print(digits[0:8])
    
    
        
