#!/usr/bin/env python3

min_n = 130254
max_n = 678275

n = 133332

count = 0
while n < max_n:
    n += 1
    de = [int(x) for x in str(n)][:]
    if not ((de[0]<=de[1]) and (de[1]<=de[2]) and (de[2]<=de[3]) and (de[3]<=de[4]) and (de[4]<=de[5])):
        continue
    if not ((de[0]==de[1]) or (de[1]==de[2]) or (de[2]==de[3]) or (de[3]==de[4]) or (de[4]==de[5])):
        continue
    print(de)
    count += 1

print(count)
    
    

    