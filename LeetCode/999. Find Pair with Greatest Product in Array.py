#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:44:59 2019

@author: Rycemond
"""

"""
1. sort, then remove {0, 1}, then check from right and left
"""

nums = [10, 3, 5, 30, 35]
 
nums = set(sorted(nums))
l, r = 0, len(nums)-1

while l < r:
    
