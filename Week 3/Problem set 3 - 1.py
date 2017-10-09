#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:05:38 2017

@author: mar
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    aDict = {}
    for letter in lettersGuessed:
        if letter not in aDict:
            aDict[letter] = letter
    secretWordletters = list(secretWord)
    for letter in secretWordletters:
        if letter in aDict:
            continue
        else:
            return False
    return True

