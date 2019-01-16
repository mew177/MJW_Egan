#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:46:00 2019

@author: Rycemond
"""
import math
import collections

def primeFactor(n):
    primes = collections.defaultdict(int)
    while n % 2 == 0:
        if 2 not in primes:
            primes[2] = 0
        primes[2] += 1 
        n /= 2
    
    for i in range(3, int(math.sqrt(n)+1), 2):
        while n % i == 0:
            if i not in primes:
                primes[i] = 0
            primes[i] += 1
            n /= i
    if n > 2:
        primes[int(n)] = 1
    return primes
    

print(primeFactor(315))
        
        