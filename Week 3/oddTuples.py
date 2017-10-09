#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:36:07 2017

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