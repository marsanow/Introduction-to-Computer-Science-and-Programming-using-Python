#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:42:35 2017

@author: mar
"""

          
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number 
    of times in L. If no such element exists, returns None 
    """
    numbers = {}
    for n in L:
        if n in numbers:
            numbers[n] += 1
        else:
            numbers[n] = 1
    newList = []
    for key, value in numbers.items():
        if value % 2 != 0:
            newList.append(key)
    newList.sort()
    if len(newList) == 0:
        return None
    else:
        return newList[-1] 
        

