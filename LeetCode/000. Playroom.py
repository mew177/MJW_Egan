#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:03:50 2018

@author: Rycemond
"""

nums = [1,3,1,1,4,6]


L = [-1 for _ in range(len(nums))] 
L[0] = nums[0]
L[1] = max(nums[0], nums[1])
        
for i in range(2,len(nums)):
    L[i] = max(L[i-1], nums[i] + L[i-2])
print(L)