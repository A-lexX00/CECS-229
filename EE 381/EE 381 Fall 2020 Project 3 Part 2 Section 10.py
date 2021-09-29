# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:07:52 2020

@author: alexb
"""

"""
# EE 381 fall 2020 Project 3 Part 2
# Name: Alex Banh
# ID: 015428502
# Start Date: 9-23-2020
# End Date: 
# Simulation of a discrete Markov chain.
"""

step = [] # List to record movement of particle

import random

p_A = float(input("Enter thr probability of going from '0' to '1'. "))
p_B = float(input("Enter thr probability of going from '1' to '0'. "))

S = int(input("Enter either '0' or '1' for the starting location. "))

step.append(S) # Recoding starting point.

#-------------------------------------------------------
for i in range(24): # Twenty-five steps total.
    r = random.uniform(0,1)
    if r < p_A and S == 0: # At node zero flip coin A
        S = 1 # Reassign node.
    elif r < p_B and S == 1: # At node one flip coin B.
        S = 0 # Reassign node.
    step.append(S)
#-------------------------------------------------------
    
for i in step:
    print(i, end = ' ') # Print target variable.