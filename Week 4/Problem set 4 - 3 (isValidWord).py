#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:53:31 2017

@author: mar
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    copiedHand = hand.copy()
    if word in wordList:
        for letter in word:
            if letter in copiedHand:
                if copiedHand[letter] > 1:
                    copiedHand[letter] -= 1
                else:
                    del copiedHand[letter]
            else: 
                return False
        return True
    else:
        return False
