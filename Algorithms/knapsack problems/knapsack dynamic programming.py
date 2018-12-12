#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Knapsack problem with dynamic programming 
Created on Sat Nov 17 12:00:32 2018
@author: Egan Wu
"""

def printBoard(bags):
    for row in bags:
        print(row)
    print("============================")

def Knapsack(items, L):
    Bag = [[0 for _ in range(L)] for _ in range(len(items))]
    
    for i in range(1, len(items)):
        for l in range(1, L):
            if weights[items[i]] > l:   
                # this item has weight larger than capacity
                Bag[i][l] = Bag[i-1][l]
            else:
                # can afford this item. Either take this or not
                Bag[i][l] = max(Bag[i-1][l], Bag[i-1][l-weights[items[i]]]+values[items[i]])
    printBoard(Bag)
        
    return Bag[len(items)-1][L-1]


items =     [0,  1, 2,  3, 4, 5,  6,  7, 8, 9, 10]
weights =   [10, 5, 6, 16, 3, 2, 12, 22, 1, 5,  2]
values =    [8,  2, 5, 15, 3, 4,  3, 15, 3, 6,  6]
L = 25

print("Maximum value is: " + (str)(Knapsack(items, L)))

