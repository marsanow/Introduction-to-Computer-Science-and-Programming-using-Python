#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:25:28 2017

@author: mar
"""

"""
Examples:
L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] then 
is_list_permutation returns (1, 3, <class 'int'>)
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    dict1 = {} 
    dict2 = {}
    for item in L1:
        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1
    for item in L2:
        if item in dict2:
            dict2[item] += 1
        else:
            dict2[item] = 1
    if dict1 != dict2:
        return False
    else:  
        dict1_sorted = sorted(dict1.items(), key=lambda x: x[1])
        return(dict1_sorted[-1][0] if len(L1) > 0 else None, dict1_sorted[-1][1] if len(L1) > 0 else None, type(dict1_sorted[-1][0]) if len(L1) > 0 else None)


