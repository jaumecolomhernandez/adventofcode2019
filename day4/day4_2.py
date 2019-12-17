#!/usr/bin/env python3

min_n = 130254
max_n = 678275

n = 133332

def runlength(text):
    en = {el:0 for key in text}
    
count = 0
while n < max_n:
    n += 1

    # Check if factors are in crescent order
    de = [int(x) for x in str(n)][:]
    if not ((de[0]<=de[1]) and (de[1]<=de[2]) and (de[2]<=de[3]) and (de[3]<=de[4]) and (de[4]<=de[5])):
        continue
    # Check if there is a pair of the same number side by side
    en = {}
    for letter in str(n): en[letter] = en.get(letter, 0) + 1    # Count number of occurences
    eq2 = [1 for a in en.values() if a == 2]    # And check if it is 2 (bc it is ascendent no problems)
    if sum(eq2) == 0:   # At least one
        continue
    
    count += 1
    
print(count)
    
    

    