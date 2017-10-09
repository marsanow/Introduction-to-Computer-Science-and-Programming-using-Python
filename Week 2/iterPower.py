#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:45:13 2017

@author: mar
"""

def iterPower(base, exp):
    """
    An iterative function that calculates the exponential base^exp by simply using 
    successive multiplication.
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    """
    total = 1
    for i in range(1, exp+1):
        total *= base
    return total

