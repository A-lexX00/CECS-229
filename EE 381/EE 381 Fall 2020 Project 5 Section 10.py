# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:26:45 2020

@author: alexb
"""

"""
# EE 381 fall 2020 Project 5
# Name: Alex Banh
# ID: 015428502
# Start Date: 11-16-2020
# End Date: 11-18-2020
# Moving forward with steps
"""

import random

S = int(input('Starting position? '))
N = int(input('What is the last state? '))
J = int(input("How many steps will be taken? "))
P = float(input('What is the probability of moving forward? '))
print(S)
for i in range(J):
    if S == 0:
        S = 1
    elif S == N:
        S = N - 1
    elif (S < N) and (S > 0):
        r = random.uniform(0,1)
        if r < P:
            S = S + 1
        else:
            S = S - 1
    print(S)