#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:46:30 2017

@author: mar
"""

def gcdIter(a, b):
    """
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    """
    maxVal = max(a, b)
    minVal = min(a, b)
    end = 0
    if minVal == 0:
        return maxVal    
    while minVal != 0:
        if a % minVal == 0 and b % minVal == 0:
            end = minVal
            break
        else:
            minVal -= 1
    return end

