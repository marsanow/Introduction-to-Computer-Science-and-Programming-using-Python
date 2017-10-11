#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:52:04 2017

@author: mar
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    copiedHand = hand.copy()
    for letter in word:
        if letter in copiedHand:
            if copiedHand[letter] > 1:
                copiedHand[letter] -= 1
            else:
                del copiedHand[letter]
    return copiedHand
