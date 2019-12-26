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
    
    digits = "03036732577212944063491565474664"
    digits = list(map(int,digits))*1000
    digits = np.array(digits,dtype=int)
    print(digits.shape)
    base = base_pattern(len(digits)+1)
    print(base)
    
    for _ in range(100):
        digits = compute_next(digits, base)
        print(digits[0:8])
    print(digits[0:8])
    
    
        
