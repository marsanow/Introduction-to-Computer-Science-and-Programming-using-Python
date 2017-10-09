#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:36:48 2017

@author: mar
"""

def how_many(aDict):
    """
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    """
    total = 0
    for key in aDict:
        total += len(aDict[key]) 
    return total