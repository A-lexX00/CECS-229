# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:29:46 2020

@author: alexb
"""

"""
# EE 381 fall 2020 Project 2
# Name: Alex Banh
# ID: 015428502
# Start Date: 9-9-2020
# End Date: 
# Simulation of a coin flip. Using simulation to determine probability
# of first heads on an odd toss.
"""

import random

p = 0.5 # Fair Coin
game = [] # Record of one game
win = 0 # Accumulator for number of wins

N = 100000

for i in range(N):

    Coin = 0 # Initial value
    
    #----------------------------------------------------------
    # Simulation
    while Coin != 1:
        r = random.uniform(0,1)
        if r < p:
            Coin = 0 # Tails
        else:
            Coin = 1 # Heads
        game.append(Coin) # List of flips per game
    L = len(game) # On last iteration number of flips
    if L % 2 == 1: # Did it happen on an odd flip 
        win = win + 1 # Total number of wins
    game = [] # Reset
    # End Simulation
    #----------------------------------------------------------
print('Toss a coin until you get heads \
the probability the head is on an odd number flip is ',win/N,'.')
