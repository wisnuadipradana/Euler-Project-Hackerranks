# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 02:57:16 2020

@author: uzumakinagato
"""

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = (n-1)//3; j = (n-1)//5; k = (n-1)//15
    bagi3 = (3*(i+1)*i)//2
    bagi5 = (5*(j+1)*j)//2
    bagi15 = (15*(k+1)*k)//2
    sum = bagi3 + bagi5 - bagi15
    print(sum) 
    

    
    
    
    
    
    
    
    
    
    
    
