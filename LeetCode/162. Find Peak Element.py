#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:19:28 2019

@author: Rycemond
"""

"""
        1. simple tranverse - O(n) (93%)
        2. recursive search - O(n)  (93%)
        { every local peek in each interval is a 
        candidate of global peek }
        3. recursive binary search - O(log(n)) (100%)
        """
        
        def biSearch(l, r):
            if l == r:
                return l
            mid = (l + r) / 2
            if nums[mid] > nums[mid+1]:
                return biSearch(l, mid)
            return biSearch(mid+1, r)
        
        return biSearch(0, len(nums)-1)
        
        """
        nums = [-float('Inf')] + nums + [-float('Inf')]
        
        def localMax(start, end):
            mid = (start + end) / 2
            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid-1
            elif nums[mid-1] > nums[mid]:
                return localMax(start, mid)
            elif nums[mid+1] > nums[mid]:
                return localMax(mid, end)
            else:
                localMax(start, mid)
                localMax(mid, end)
        return localMax(0, len(nums)-1)
                
        """
        
        """
        localMax = 0
        for i in range(len(nums)):
            if nums[localMax] <= nums[i]:
                localMax = i
            else:
                return localMax
        return localMax # handle len(nums) == 1
        """