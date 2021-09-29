# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:47:49 2020

@author: alexb
"""

"""
# EE 381 fall 2020 Project 3 Part 1
# Name: Alex Banh
# ID: 015428502
# Start Date: 9-23-2020
# End Date: 
# Simulation of a Bernoulli RV.
"""

import random

p = float(input('Enter the probablilty of success. ')) # Enter probability
T = int(input('Enter the number of trials. ')) # Number of experiments

for i in range(T):
    
    r = random.uniform(0,1) # Random number generation
    
    if r < p: # Test for success.
        print('1',end=' ') # Formatted to print on same line
    else:
        print('0',end=' ') # Formatted like above