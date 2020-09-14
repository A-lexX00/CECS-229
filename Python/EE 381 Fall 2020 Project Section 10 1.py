# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:32:05 2020

@author: alexb
"""

""" ----------------------------------------------------
# EE 381 fall 2020 Project 1
# Name: Alex Banh
# ID: 015428502
# Start Date: 8-26-2020
# End Date: 8-31-2020
# This program is a pseudorandom number generator.
# It will be used to do simple simulations.
---------------------------------------------------- """ 

def main(): # Main module
    
    def RNG(): # Random Number Generator
        r = [] # Empty list for random numbers
        N = 10000 # Cycle length or norm
        A = 4857 # Adder
        M = 8601 # Multiplier
        
        S = int(input('Enter a whole number.')) # Inputing seed
        
        for i in range(100):
            S = (M * S + A) % N # Linear Congruential Generator
            s = S/N # r is in [0,1)
            r.append(s)
        return r
    
    def Die(r):
        print('Die Roll Below')
        import math
        for k in range(25):
            d = math.floor(6 * r[k] + 1)
            print(d)
    def Coin(r):
        print('Die Coin Toss')
        import math
        for k in range(25):
            c = math.floor(2 * r[k])
            if (c == 0):
                print('Tails')
            else:
                print('Heads')
                
    t= RNG() # Call random number generator and get list
    Die(t)
    Coin(t)
main()