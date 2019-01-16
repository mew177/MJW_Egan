#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:17:34 2019

@author: Rycemond
"""

"""
        1. search from left and right, choose less - O(3n)
        2. optimization of above - O(2n), (76%)
        """
        
        leftHeight, rightHeight, leng = 0, 0, len(height)
        leftTrap, rightTrap, trap = [], [], 0
        for i in range(len(height)):
            if height[i] >= leftHeight:
                leftHeight = height[i]
                leftTrap.append(0)
            else:
                leftTrap.append(leftHeight - height[i])
            
            if height[leng-i-1] >= rightHeight:
                rightHeight = height[leng-i-1]
                rightTrap.append(0)
            else:
                rightTrap.append(rightHeight - height[leng-i-1])
                
        rightTrap = rightTrap[::-1]
        for i in range(leng):
            trap += min(leftTrap[i], rightTrap[i])
        return trap
        
        
        """
        lastHeight = 0
        leftTrap, rightTrap, trap = [], [], 0
        for i in range(len(height)):
            if height[i] >= lastHeight:
                lastHeight = height[i]
                leftTrap.append(0)
            else:
                leftTrap.append(lastHeight - height[i])
        
        lastHeight = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] >= lastHeight:
                lastHeight = height[i]
                rightTrap.append(0)
            else:
                rightTrap.append(lastHeight - height[i])
        rightTrap = rightTrap[::-1]
        for i in range(len(height)):
            trap += min(leftTrap[i], rightTrap[i])
        
        print(leftTrap)
        print(rightTrap[::-1])
        
        return trap
        """