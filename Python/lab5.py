# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:13:32 2020

@author: alexb
"""

def translate(S, z0):
    """
    translates the complex numbers of set S by z0
    INPUT: 
        * S - set of complex numbers
        * z0 - complex number
    OUT:
        * T - set consisting of points in S translated by z0
    """
    #FIXME: IMPLEMENT FUNCTION
    T = []
    for z in S:
        T.append(z0 + z)
    return set(T)

def scale(S, k):
    """
    scales the complex numbers of set S by k.  
    INPUT: 
        * S - set of complex numbers
        * k - positive float, raises ValueError if k <= 0
    OUT:
        * T - set consisting of points in S scaled by k
        
    """
    #FIXME: IMPLEMENT FUNCTION
    T = []
    if (k <= 0):
        raise ValueError("Not a positive float value")
    else:
        for i in S:
            T.append(i * k)
    return set(T)

def rotate(S, theta):
    """
    rotates the complex numbers of set S by theta radians.  
    INPUT: 
        * S - set of complex numbers
        * theta - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. 
        If zero, no rotation.
    OUT:
        * T - set consisting of points in S rotated by theta radians
        
    """
    #FIXME: IMPLEMENT FUNCTION
    from math import e, pi
    T = []
    if(theta == 0):
        return S
    else:
        degree = theta * 1j
        for z in S:
            z = e**(degree)*z
            T.append(z)
        return set(T)