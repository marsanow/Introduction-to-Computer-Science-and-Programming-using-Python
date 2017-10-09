#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 21:27:56 2017

@author: martuska
"""

"""
A program that counts up the number of vowels contained in the string
Example: 
    s = 'azcbobobegghakl' should print 'Number of vowels: 5'
"""
count = 0
for i in s:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1
print("Number of vowels: " + str(count))