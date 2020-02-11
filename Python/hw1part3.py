# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:15:28 2020

@author: alexb
"""

def gcd(a,b):
    #FIXME: IMPLEMENT THIS METHOD
    if (b != 0):
        return gcd(b, a%b)
    else:
        return a