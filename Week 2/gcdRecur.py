#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:47:17 2017

@author: mar
"""

def gcdRecur(a, b):
    """
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    (idea from Euclid's algorithm)
    """
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
    
    