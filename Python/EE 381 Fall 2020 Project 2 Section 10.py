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

p = 0.5

for i in range(10):
    r = random.uniform(0, 1)
    if r < p:
        print('T')
    else:
        print('H')