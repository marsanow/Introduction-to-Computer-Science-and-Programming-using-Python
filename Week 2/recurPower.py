#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:45:41 2017

@author: mar
"""

def recurPower(base, exp):
    """
    A recursive function for iterPower
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    elif exp == 1:
        return 1 * base
    else:
        return base * recurPower(base, exp - 1)
    
    