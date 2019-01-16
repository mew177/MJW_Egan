#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:21:52 2019

@author: Rycemond
"""

"""
        1. brute force - n!
        2. * single pass - n
        """
        
        # find first element from right that is not in incrementing order
        idx1 = len(nums)-1
        while idx1 > 0:
            idx1 -= 1
            if nums[idx1] < nums[idx1+1]:
                break
        # find first element from idx1 that is not in decrementing order
        idx2 = idx1 + 1
        while idx2 < len(nums):
            if nums[idx2] <= nums[idx1]:
                break
            idx2 += 1
        nums[idx1], nums[idx2-1] = nums[idx2-1], nums[idx1]
        
        # reverse
        if idx2 == idx1 + 1:
            nums.reverse()
        else:
            nums[idx1+1:len(nums)] = nums[idx1+1:len(nums)][::-1]