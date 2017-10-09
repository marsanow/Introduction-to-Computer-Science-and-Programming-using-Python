#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 22:38:29 2017

@author: mar
"""

def minPayment(balance, annualInterestRate, monthlyPaymentRate):
    """
    A program to calculate the credit card balance after one year if a person 
    only pays the minimum monthly payment required by the credit card company 
    each month.
    Variables:
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPaymentRate - minimum monthly payment rate as a decimal
    """
    months = 1
    while months < 13:
        balance -= balance*monthlyPaymentRate
        balance += balance*(annualInterestRate/12)
        months += 1
    print("Remaining balance: " + str(round(balance, 2)))

