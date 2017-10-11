#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 12:56:59 2017

@author: mar
"""
"""
If d = {1:10, 2:20, 3:30}
    then {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} 
    then {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} 
    then {True: [0, 2, 4]}
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    newList = []
    for key, value in d.items():
        newList.append([value, key])
    sortedList = sorted(newList)
    newDict = {}
    for item in sortedList:
        if item[0] not in newDict.keys():
            newDict[item[0]] = [item[1]]
        else:
            newDict[item[0]].append(item[1])
    print(newDict)
            
