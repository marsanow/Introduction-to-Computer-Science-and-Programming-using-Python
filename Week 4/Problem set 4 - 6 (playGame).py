#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:11:31 2017

@author: mar
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    newHand = {}
    userResponse = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    while userResponse != "e":
    #Enter n to deal a new hand, r to replay the last hand, or e to end game:
        # if n:
        if userResponse == "n":
            #deal hand
            newHand = dealHand(HAND_SIZE)
            #playHand
            playHand(newHand, wordList, HAND_SIZE)
        # if r: 
        elif userResponse == "r":
            # if no stored hands, error, ask again
            if newHand == {}:
                print("You have not played a hand yet. Please play a new hand first!")
            #replay the old hand
            else:
                playHand(newHand, wordList, HAND_SIZE)
        elif userResponse == "e":
            break
        # if anything else:
        else:
            #invalid cmmand. ask again 
            print("Invalid command.")
        userResponse = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
