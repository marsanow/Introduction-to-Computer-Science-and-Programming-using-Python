#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 15:38:52 2017

@author: mar
"""

"""
A program that prints the number of times the string 'bob' occurs in s
    Input: a lowercase string
    Output: a number of times 'bob' occurs
Example: s = 'azcbobobeggbobhakl' should print 'Number of times bob occurs is: 2'
"""

count = 0
total = 0
for letter in s:
    count += 1
    if letter == 'b':
       if s[count-1:count+2] == 'bob':
            total += 1
print('Number of times bob occurs is: ' + str(total))
