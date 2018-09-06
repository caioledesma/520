#!/usr/bin/python3 

from random import randint
numeros = [12, 56, 54, 21, 48, 513, 465, 84, 5469]
par = [x for x in numeros if x % 2 == 0] 
#par = []
#for x in numeros:
#    par.append(x)

print(par)
#print(randint(4))
