# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:10:54 2020

@author: uzumakinagato
"""

import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum([int(i) for i in str(math.factorial(n))]))
