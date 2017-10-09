#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 10:17:20 2017

@author: mar
"""

def oddTuples(aTup):
    """
    aTup: a tuple
    returns: tuple, every other element of aTup.
    """
    count = 1
    newTup = ()
    for i in aTup:
        if count % 2 != 0:
            newTup += (i,)
        count += 1
    return newTup


def how_many(aDict):
    """
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    """
    total = 0
    for key in aDict:
        total += len(aDict[key]) 
    return total

