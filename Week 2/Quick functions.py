#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:41:24 2017

@author: mar
"""

def square(x):
    '''
    x: int or float.
    '''
    return x ** 2

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * x ** 2 + b * x + c

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return(x % 2 ==1)

