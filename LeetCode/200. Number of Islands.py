#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 16:17:50 2019

@author: Rycemond
"""

maps = [[1, 1, 1, 0, 0],
        [1, 0, 1, 0, 3],
        [1, 0, 0, 2, 0],
        [0, 4, 0, 0, 0],
        [4, 4, 4, 0, 5]]


def dfs(r, c):
    rows = len(maps)
    cols = len(maps[0])
    
    if r < 0 or r >= rows or c < 0 or c >= cols or maps[r][c] == 0:
        return 
    
    maps[r][c] = 0
    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)
 
islands = 0
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] != 0:
            islands += 1
            dfs(i, j)
print(islands)
    
    
    
    
