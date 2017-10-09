#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 22:41:05 2017

@author: mar
"""

def fixedPayment(balance, annualInterestRate):
    """
    A program that calculates the minimum fixed monthly payment needed in order
    pay off a credit card balance within 12 months.
    Variables:
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    """
    originalBalance = balance
    minMonthlyPayment = 0.01
    monthlyInterest = annualInterestRate/12
    while balance >= originalBalance:
        month = 12
        while month > 0:
            balance -= minMonthlyPayment
            balance += balance*monthlyInterest
            month -= 1	
            if balance < 0:
                print("Lowest payment:", str(minMonthlyPayment))
                break
        else:
            minMonthlyPayment += 0.01
            month = 12
            balance = originalBalance

