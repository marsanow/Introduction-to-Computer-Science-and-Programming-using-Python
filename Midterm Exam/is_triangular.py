#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:47:27 2017

@author: mar
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    example:  1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., 
    are triangular numbers.
    """
    if k == 1:
        return True
    elif k == 2:
        return False
    else:
        number = 0
        for i in range(1, k):
            number += i
            if number == k:
                return True
                break
            elif number < k:
                continue
            else:
                return False

