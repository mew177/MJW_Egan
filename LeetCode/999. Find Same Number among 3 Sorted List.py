#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 12:53:34 2019

@author: Rycemond
"""

"""
1. each list a pointer search from left to right
2. right shift pointer for smallest number 
"""

list1 = [20, 20, 33, 50, 78, 98, 102, 105]
list2 = [20, 33, 53, 73, 76, 78, 99, 105]
list3 = [21, 33, 43, 53, 78, 102, 105]
ans = []

l1, l2, l3 = 0, 0, 0

while l1 < len(list1) and l2 < len(list2) and l3 < len(list3):
    
    if list1[l1] == list2[l2] and list2[l2] == list3[l3]:
        ans.append(list1[l1])
        l1+=1
        l2+=1
        l3+=1
    elif list1[l1] < list2[l2]:
        l1+=1
    elif list2[l2] < list3[l3]:
        l2+=1
    else:
        l3+=1
        
print(ans)

        

