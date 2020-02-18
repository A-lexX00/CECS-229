# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:04:35 2020

@author: alexb
"""

def bezoutCoeffs(a, b):
    #FIXME: IMPLEMENT THIS METHOD.
    s0, s1, t0, t1, = 0, 1, 1, 0
    while a != 0:
        q = b // a
        a, b = b % a, a
        s0, s1 = s1, s0 - (q * s1)
        t0, t1 = t1, t0 - (q * t1)
    return (s0, t0)

    # I was trying out the numbers you had given us
    # in the algorithm from the hint but I could not
    # get it to work with those numbers so I found a
    # different solution set online on the website
    # https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    # I tried hard to get it to work but I only got it
    # to work with these sets of numbers
    """s0, s1, t0, t1, = 1, -1 * (b // a), 0, 1
    while a != 0:
        q = b // a
        a, b = b % a, a
        s0, s1 = s1, s0 - (q * s1)
        t0, t1 = t1, t0 - (q * t1)
    return (s1, t1)"""