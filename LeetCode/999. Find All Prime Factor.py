#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 01:53:44 2019

@author: Rycemond
"""

n = 9
factor = [1 for _ in range(n+1)]
factor[0], factor[1] = 0, 0

for i in range(2, n+1):
    if i:
        if n % i == 0:
            for k in range(i**2, n+1, i):
                factor[k] = 0
        else:
            factor[i] = 0
print(factor)