#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:47:54 2017

@author: mar
"""

def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    """
    testChar = len(aStr)//2
    if len(aStr) == 0:
        return aStr == char
    elif len(aStr) == 1:
        return aStr == char
    else:
        if char == aStr[testChar]:
            return True
        elif char > aStr[testChar-1:testChar]:
            return isIn(char, aStr[testChar +1:])
        else:
            return isIn(char, aStr[:testChar])
        
        