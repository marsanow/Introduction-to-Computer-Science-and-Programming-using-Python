#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:10:57 2017

@author: mar
"""

"""
A program that guesses a secret number (using bisection search).
Input: User input is an integer x, when 0 <= x < 100
Output: The secret number.

Example session:
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is
too low. Enter 'c' to indicate I guessed correctly. c
"""

low = 0
high = 100
ans = (high + low) // 2

print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(ans) + "?")
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )
while guess != "c":
    if guess == "h":
        high = ans
    elif guess == "l":
        low = ans
    else:
        print("Sorry, I did not understand your input.")
    ans = (high + low) // 2
    print("Is your secret number " + str(ans) + "?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )
if guess == "c":
    print("Game over. Your secret number was: " + str(ans))

