#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:08:28 2017

@author: mar
"""

def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    import string
    alphabet = list(string.ascii_lowercase)
    notGuessed = ""
    for letter in alphabet:
        if letter in lettersGuessed:
            continue
        else: 
            notGuessed += letter
    return notGuessed

