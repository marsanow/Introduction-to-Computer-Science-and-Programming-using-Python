#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:09:51 2017

@author: mar
"""

def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', str(len(secretWord)), 'letters long')
    
    lettersGuessed = []
    count = 8
    while count > 0:
        print('-----------')
        print('You have', str(count), 'guesses left')
        print('Available Letters:', getAvailableLetters(lettersGuessed))
        userGuessInput = input('Please guess a letter: ')
        userGuess = userGuessInput.lower()
        if userGuess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            continue
        elif userGuess not in lettersGuessed:
            if userGuess in secretWord:
                lettersGuessed += userGuess
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print('-----------')
                    print("Congratulations, you won!")
                    break
            else:
                count -= 1
                lettersGuessed += userGuess
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)) 
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print('-----------')
        print("Sorry, you ran out of guesses. The word was", secretWord + ".")


            
