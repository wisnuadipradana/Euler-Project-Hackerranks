# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:45:18 2020

@author: uzumakinagato
"""

def max_prime_factor(x): 
    maxPrime = -1

    while x % 2 == 0: 
        maxPrime = 2
        x >>= 1 # equivalent to n //= 2
    
    for i in range(3, int(x**.5) + 1, 2): 
        while x % i == 0: 
            maxPrime = i 
            x //= i 
    
    return x if x > 2 else maxPrime
  

t = int(input().strip())
for _ in range(t): 
    n = int(input().strip())
    print(max_prime_factor(n))
