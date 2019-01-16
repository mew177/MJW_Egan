#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 23:19:58 2019

@author: Rycemond
"""

"""
        1. linear search up to sqrt(n) - O(n^n), runtime_error
        2. optimization - O(n^0.5), (73%)
        """
        
        if n < 2:
            return 0
        
        isPrime = [1 for _ in range(n)]
        for i in range(2, int(n**0.5)+1):
            if isPrime[i]:
                for x in range(i**2, n, i):
                    isPrime[x] = 0
        return sum(isPrime[2:])
        
        """
        def isPrime(n, count=0):
            if n < 2:
                return count
            elif n == 2:
                return isPrime(n-1, count+1)
            else:
                if n % 2 == 0:
                    return isPrime(n-1, count)
                for i in range(2, int(math.sqrt(n)+1)):
                    if n % i == 0:
                        return isPrime(n-1, count)
                return isPrime(n-1, count+1)
        
        return (isPrime(n))
        """