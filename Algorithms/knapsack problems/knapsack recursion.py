#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
## Knapsack problem with recursive algorithm
Created on Sat Nov 17 11:38:18 2018
@author: Egan Wu
"""

def Knapsack(items, L):
    if len(items) == 0:
        # not item can choose
        return 0
    
    if weights[items[0]] > L:
        # This item has weight larger than capacity, so discard it. 
        return Knapsack(items[1:len(items)], L)
    else:
        # either take this item or not
        # if this item is taken, then capacity is reduced
        return max(Knapsack(items[1:len(items)], L), Knapsack(items[1:len(items)], L-weights[items[0]])+values[items[0]])
    

items =     [0,  1, 2,  3, 4, 5,  6,  7, 8, 9, 10]
weights =   [10, 5, 6, 16, 3, 2, 12, 22, 1, 5,  2]
values =    [8,  2, 5, 15, 3, 4,  3, 15, 3, 6,  6]
L = 25


print("Maximum value is: " + (str)(Knapsack(items, L)))

"""
Time complexity:
    Whenever a node (Xi) is determined, algorithm constructed a tree containing 2^(i) nodes.
    That is to say, when a (Xn) node is determinded, algorithm needs to construct a tree with 2^(n) nodes
    So, this algorithm takes O(2^n) time to finish.
"""