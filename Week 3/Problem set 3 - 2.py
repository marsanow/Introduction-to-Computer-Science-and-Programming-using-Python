#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:07:22 2017

@author: mar
"""

def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    """
    aDict = {}
    for letter in lettersGuessed:
        if letter not in aDict:
            aDict[letter] = letter
    secretWordletters = list(secretWord)
    wordBeingGuessed = ""
    for letter in secretWordletters:
        if letter in aDict:
            wordBeingGuessed += letter
        else:
            wordBeingGuessed += "_ "
    return wordBeingGuessed

