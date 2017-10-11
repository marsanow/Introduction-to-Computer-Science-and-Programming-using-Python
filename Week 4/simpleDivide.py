#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:44:43 2017

@author: mar
"""

def simple_divide(item, denom):
   try:
       return item / denom
   except ZeroDivisionError:
       return 0