#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 10:38:17 2017

@author: martuska
"""


"""
A program that prints the longest substring of s in which the letters occur in 
alphabetical order.
Example 1:
    Input: s = 'azcbobobegghakl'
    Output: Longest substring in alphabetical order is: beggh
Example 2: (in case of a tie, print the first one)
    Input: s = 'abcbcd'
    Output: Longest substring in alphabetical order is: abc 
"""

longestSoFar = ""
currentSubstring = ""
count = 0
iteration = 0
for letter in s:
    count += 1
    if iteration == 0:
        if letter <= s[count:count+1]:
            longestSoFar += letter
        elif letter == s[-1:] and letter > s[count:count-1]:
            longestSoFar += letter
        elif letter >= s[count:count+1] and s[count:count+1] <= s[count:count+2]:
            longestSoFar += letter
            iteration += 1
            continue
    else:
        if letter <= s[count:count+1]:
            currentSubstring += letter
        elif letter == s[-1:] and letter > s[count:count-1]:
            currentSubstring += letter
            if len(longestSoFar) >= len(currentSubstring):
                longestSoFar = longestSoFar
                currentSubstring = ""
                continue
            else:
                longestSoFar = currentSubstring
                currentSubstring = ""
                continue
        elif letter >= s[count:count+1] and s[count:count+1] <= s[count:count+2]:
            currentSubstring += letter
            if len(longestSoFar) >= len(currentSubstring):
                longestSoFar = longestSoFar
                currentSubstring = ""
                continue
            else:
                longestSoFar = currentSubstring
                currentSubstring = ""
                continue
print("Longest substring in alphabetical order is: " + str(longestSoFar))














