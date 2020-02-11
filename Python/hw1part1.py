# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:33:31 2020

@author: alexb
"""

def modExp(b, n, m):
    #FIXME: IMPLEMENT THIS METHOD
    # if the modular is 1
    if (m == 1):
        return 0
    # basis of loop
    c = 1
    # 
    expoCounter = 0
    # pass through the algorithm for each exponent
    # works because 
    #   through Corollary 4.1.4
    #   (b^n) mod m = [(x) mod m) * ((y) mod m)] mod m
    #       x = b^r & y = b^q
    #           Where r = n - m & q = n - r
    #               while m < n & m is an integer SO
    #   c mod m = (a * b) mod m 
    #       Where c = b^n & a = x mod m & b = y mod m
    #   c mod m = [(a mod m) * (b mod m)] mod m
    #       SO by Corollary 4.1.4
    #   c mod m = (a * b) mod m
    for expoCounter in range(0, n):
        # c = (b * c) mod m
        # works because with the proof eariler
        # (b^n) mod m = (b * c) mod m
        c = (c * b) % m
    return c