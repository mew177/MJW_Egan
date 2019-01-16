#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:20:55 2019

@author: Rycemond
"""

"""
        sums = [[0 for _ in nums] for _ in nums]
        count = 0
        
        # initializatoion
        for i in range(len(nums)):
            sums[i][i] = nums[i]
        
        for start in range(len(nums)-1, -1, -1):
            for end in range(start, len(nums)):
                if start == end:
                    sums[start][end] = nums[end]
                elif end > start:
                    sums[start][end] = sums[start][end-1] + nums[end]
                if sums[start][end] == k:
                    count += 1
                    
        #for row in sums:
        #    print(row)
        return count
        
        """
        
        """
        1. brute force - n!, time limit exceed
        2. dynamic programming - n^2 , space limit exceed
        3. hashmap - n, 
        """
        
        """
        count, size = 0, len(nums)
        sums = [0 for _ in range(len(nums)+1)]
        
        for i in range(1, len(nums)+1):
            sums[i] = sums[i-1] + nums[i-1]
        
        for start in range(len(nums)):
            for end in range(start+1, len(nums)+1):
                if sums[end] - sums[start] == k:
                    count += 1                    
        return count
        """
        
        table = collections.defaultdict(int)
        sums, count = 0, 0
        table[0] = 1
        
        for num in nums:
            sums += num
            if (sums-k) in table:
                count += table[sums-k]
                
            tempSum = 1
            if sums in table:    
                tempSum += table[sums]
            table[sums] = tempSum 
        return count
        