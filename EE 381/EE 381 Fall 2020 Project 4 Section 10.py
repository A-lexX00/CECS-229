# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:16:36 2020

@author: alexb
"""

"""
# EE 381 fall 2020 Project 4
# Name: Alex Banh
# ID: 015428502
# Start Date: 10-26-2020
# End Date: 
# Simulating a continuous uniform RV
"""

import math # Math functions in program
import random # Use pseudorandom numbers
import matplotlib.pyplot as pdf # Graphics alias pdf, probability density function.

n = 10000 # Number of random numbers.
Lambda = 1 # Parameter for exponential RV
x = [] # List for uniformally distributed random numbers.
y = [] # List for exponentially distrubuted random numbers.

for i in range(n): # Creating the list of numbers.
    r = random.uniform(0,1)
    x.append(r) # The list of uniformally distributed random numbers.
    e = -(1/Lambda) * math.log(1 - r, math.e)
    y.append(e)
    
b = max(x)
a = min(x)
R = b - a # Range
intervals = int(math.ceil(math.sqrt(n))) # These are the classes or bins.
width = (R / intervals) # The class width.
#-------------------------------------------------------------------------
pdf.subplot(2, 1, 1)
pdf.hist(x, intervals, density = width) # Uniform Simulation.
pdf.subplot(2, 1, 2)
pdf.hist(y, intervals, density = width) # Expoential Simulation