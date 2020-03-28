#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:41:37 2019

@author: Rycemond
"""

"""
1.  if there's a number larger than rest of two numbers, then those numbers 
    are definitely uncommon among lists 
"""

list1 = [20, 20, 33, 50, 78, 98, 102]
list2 = [20, 33, 53, 73, 76, 78, 99, 105]
list3 = [21, 33, 43, 53, 78, 102]
ans = []

n1, n2, n3 = len(list1), len(list2), len(list3)
l1, l2, l3 = 0, 0, 0

dict = {}

while l1 < n1 and l2 < n2 and l3 < n3:
    
    if l1 < n1:
        try:
            dict[list1[l1]] += 1
        except KeyError:
            dict[list1[l1]] = 1
        l1 += 1
            
    if l2 < n2:
        try:
            dict[list2[l2]] += 1
        except KeyError:
            dict[list2[l2]] = 1
        l2 += 1
            
    if l3 < n3:
        try:
            dict[list1[l3]] += 1
        except KeyError:
            dict[list1[l3]] = 1
        l3 += 1              

print(dict.items)
print(list(filter(lambda x: x % 2 == 0, dict)))
     
    