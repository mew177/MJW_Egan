#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:20:17 2019

@author: Rycemond
"""

"""
        1. array substitution - O(n), space(n)
        2. zero substitutio along - O(n), space(1)
        3. reduce useless assignment - O(n), space(1)
        """
        
        lastzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastzero], nums[i] = nums[i], nums[lastzero]
                lastzero += 1
        
        """
        lastzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastzero] = nums[i]
                lastzero += 1
        for i in range(len(nums)-1, len(nums)-lastzero, -1):
            nums[i] = 0
        """  
            
        """
        size, zero, ans = len(nums), 0, []
        for num in nums:
            if num != 0:
                ans.append(num)
            else:
                zero += 1
        ans = ans + [0 for _ in range(zero)]
        for i in range(len(ans)):
            nums[i] = ans[i] 
        """