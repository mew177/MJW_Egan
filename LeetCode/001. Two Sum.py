#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 00:32:25 2019

@author: Egan Wu
"""

"""
1. brute force - n^2
2. denote complement - using list [40%]
3. denote complement - using dict [99%]
"""
import collections

nums = [0, 2, 7, 6]
target = 8
ans = [-1, -1]
        
comps = collections.defaultdict(int)   
for i in range(len(nums)):
    if nums[i] in comps:
        ans = [comps[nums[i]], i]
    else:
        comps[target - nums[i]] = i

print(ans)