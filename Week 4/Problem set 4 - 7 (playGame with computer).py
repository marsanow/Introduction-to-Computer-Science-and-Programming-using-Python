#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:12:53 2017

@author: mar
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    newHand = {}
    userResponse = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    while userResponse != "e":
    #Enter n to deal a new hand, r to replay the last hand, or e to end game:
        # if n:
        if userResponse == "n":
            while True:
                compOrHuman = input("Enter u to have yourself play, c to have the computer play: ")
                if compOrHuman == "u":
                    newHand = dealHand(HAND_SIZE)
                    playHand(newHand, wordList, HAND_SIZE)
                    break
                elif compOrHuman == "c":
                    newHand = dealHand(HAND_SIZE)
                    compPlayHand(newHand, wordList, HAND_SIZE)
                    break
                else:
                    print("Invalid command.")
            # if r: 
        elif userResponse == "r":
            # if no stored hands, error, ask again
            if newHand == {}:
                print("You have not played a hand yet. Please play a new hand first!")
            #replay the old hand
            else:
                while True:
                    compOrHuman = input("Enter u to have yourself play, c to have the computer play: ")
                    if compOrHuman == "u":
                        playHand(newHand, wordList, HAND_SIZE)
                        break
                    elif compOrHuman == "c":
                        compPlayHand(newHand, wordList, HAND_SIZE)
                        break
                    else:
                        print("Invalid command.")
        elif userResponse == "e":
            break
        # if anything else:
        else:
            #invalid command. ask again 
            print("Invalid command.")
        userResponse = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")